"""
Video KYC (proof-of-concept)

Features implemented:
 1. Motion Detection: ensures the subject is not a static image
 2. Active Liveness Detection: prompts random actions (blink, nod, turn-head, smile)
 3. Passive Liveness Detection: optical-flow micro-movements + texture (Laplacian variance + LBP histogram)
 4. Face Anti-Spoofing: rule-based checks combining texture + movement + reflection checks

Notes:
 - This is a standalone prototype using OpenCV + MediaPipe.
 - For production, use dedicated, audited anti-spoofing ML models and secure transfer/storage.

Dependencies:
 pip install opencv-python mediapipe numpy imutils
 (optional: scikit-image for LBP but implemented here without it)

Usage:
 python video_kyc.py

Press 'q' to exit.

"""

import cv2
import mediapipe as mp
import numpy as np
import time
import random
import math
from collections import deque
import imutils

# ---------------------- Utility functions ----------------------

def rect_from_landmarks(landmarks, img_w, img_h):
    xs = [int(p.x * img_w) for p in landmarks]
    ys = [int(p.y * img_h) for p in landmarks]
    x1, x2 = max(min(xs) - 10, 0), min(max(xs) + 10, img_w)
    y1, y2 = max(min(ys) - 10, 0), min(max(ys) + 10, img_h)
    return x1, y1, x2, y2


def eye_aspect_ratio(eye):
    # EAR using 6 points: p1..p6
    # eye: list of (x,y) coordinates in order
    A = math.dist(eye[1], eye[5])
    B = math.dist(eye[2], eye[4])
    C = math.dist(eye[0], eye[3])
    if C == 0:
        return 0.0
    ear = (A + B) / (2.0 * C)
    return ear


def mouth_aspect_ratio(mouth):
    # simple MAR approximation using vertical / horizontal distances
    A = math.dist(mouth[13], mouth[19])  # upper-lip to lower-lip
    C = math.dist(mouth[0], mouth[6])    # mouth width
    if C == 0:
        return 0.0
    return A / C


def lbp_image_gray(img_gray):
    # Basic uniform LBP (8 neighbors)
    h, w = img_gray.shape
    lbp = np.zeros_like(img_gray, dtype=np.uint8)
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            center = img_gray[y, x]
            code = 0
            code |= (img_gray[y - 1, x - 1] > center) << 7
            code |= (img_gray[y - 1, x] > center) << 6
            code |= (img_gray[y - 1, x + 1] > center) << 5
            code |= (img_gray[y, x + 1] > center) << 4
            code |= (img_gray[y + 1, x + 1] > center) << 3
            code |= (img_gray[y + 1, x] > center) << 2
            code |= (img_gray[y + 1, x - 1] > center) << 1
            code |= (img_gray[y, x - 1] > center) << 0
            lbp[y, x] = code
    return lbp


def hist_lbp(lbp):
    hist, _ = np.histogram(lbp.ravel(), bins=256, range=(0, 256))
    hist = hist.astype(float)
    if hist.sum() > 0:
        hist /= hist.sum()
    return hist


# ---------------------- Liveness / Anti-spoof heuristics ----------------------

class LivenessEngine:
    def __init__(self, buffer_seconds=2, fps=20):
        self.prev_gray = None
        self.prev_points = None
        self.flow_metrics = deque(maxlen=int(buffer_seconds * fps))
        self.face_motion_buffer = deque(maxlen=10)

    def motion_detected(self, face_roi_gray):
        """Use frame difference + Laplacian variance to detect if ROI is static (photo)"""
        if self.prev_gray is None:
            self.prev_gray = face_roi_gray
            return True
        diff = cv2.absdiff(face_roi_gray, self.prev_gray)
        nonzero = np.count_nonzero(diff)
        self.prev_gray = face_roi_gray
        h, w = face_roi_gray.shape
        motion_ratio = nonzero / (h * w)
        # debug: print('motion_ratio', motion_ratio)
        return motion_ratio > 0.002  # tuned threshold

    def micro_movement_score(self, frame_gray, face_rect):
        # compute sparse optical flow inside face rect
        x1, y1, x2, y2 = face_rect
        roi = frame_gray[y1:y2, x1:x2]
        if roi.size == 0:
            return 0.0
        roi = cv2.resize(roi, (160, 160))
        # detect good features
        p0 = cv2.goodFeaturesToTrack(roi, maxCorners=100, qualityLevel=0.01, minDistance=5)
        if p0 is None:
            return 0.0
        if self.prev_points is None:
            self.prev_points = p0
            self.prev_roi = roi
            return 0.0
        p1, st, err = cv2.calcOpticalFlowPyrLK(self.prev_roi, roi, self.prev_points, None)
        if p1 is None:
            return 0.0
        movement = np.linalg.norm((p1 - self.prev_points), axis=2)
        mean_mov = float(np.mean(movement))
        # push to buffer
        self.flow_metrics.append(mean_mov)
        # update prev
        self.prev_points = p1
        self.prev_roi = roi
        return np.mean(self.flow_metrics) if len(self.flow_metrics) > 0 else mean_mov

    def texture_score(self, face_roi_gray):
        # Laplacian variance: blurry printouts have low variance
        lap_var = cv2.Laplacian(face_roi_gray, cv2.CV_64F).var()
        # compute basic LBP histogram distance to uniform live pattern
        lbp = lbp_image_gray(face_roi_gray)
        h = hist_lbp(lbp)
        # compare to a nominal "live" distribution: we don't have a dataset, so use entropy as proxy
        entropy = -np.sum([p * np.log2(p) for p in h if p > 0])
        # normalize roughly
        lap_norm = min(lap_var / 1000.0, 1.0)
        ent_norm = min(entropy / 8.0, 1.0)
        # combined
        score = 0.6 * lap_norm + 0.4 * ent_norm
        return score

    def reflection_check(self, face_roi_color):
        # detect large specular highlights that often appear with screens
        hsv = cv2.cvtColor(face_roi_color, cv2.COLOR_BGR2HSV)
        v = hsv[:, :, 2]
        bright_ratio = np.count_nonzero(v > 240) / v.size
        return bright_ratio < 0.02

    def is_spoof(self, frame_gray, frame_color, face_rect):
        x1, y1, x2, y2 = face_rect
        roi_gray = frame_gray[y1:y2, x1:x2]
        roi_color = frame_color[y1:y2, x1:x2]
        if roi_gray.size == 0:
            return False, {'reason': 'no-face-roi'}
        motion = self.motion_detected(roi_gray)
        micro = self.micro_movement_score(frame_gray, face_rect)
        texture = self.texture_score(roi_gray)
        reflection = self.reflection_check(roi_color)

        # thresholds (empirical) - tune for your environment
        reasons = {}
        if not motion:
            reasons['motion'] = motion
        if micro < 0.2:
            reasons['micro_movement'] = micro
        if texture < 0.35:
            reasons['texture'] = texture
        if not reflection:
            reasons['reflection'] = True

        # simple rule: if two or more negative signals -> likely spoof
        neg_count = sum([1 for k in reasons.keys()])
        is_spoof = neg_count >= 2
        return is_spoof, {'motion': motion, 'micro': micro, 'texture': texture, 'reflection': reflection, 'reasons': reasons}


# ---------------------- Active liveness prompt engine ----------------------

class ActivePromptEngine:
    def __init__(self, prompts=None, timeout=6):
        if prompts is None:
            prompts = ['blink', 'turn_left', 'turn_right', 'nod', 'smile']
        self.prompts = prompts
        self.current = None
        self.start_time = None
        self.timeout = timeout
        self.success = False

    def next_prompt(self):
        self.current = random.choice(self.prompts)
        self.start_time = time.time()
        self.success = False
        return self.current

    def check(self, current_prompt, face_landmarks, img_w, img_h, prev_nose_x=None, prev_nose_y=None):
        # face_landmarks: normalized landmarks list from MediaPipe
        # returns (success:bool, explanation:str)
        now = time.time()
        if current_prompt is None:
            return False, 'no_prompt'
        if now - self.start_time > self.timeout:
            return False, 'timeout'

        # convert useful landmarks
        # Using FaceMesh landmark indices (MediaPipe) to get eyes, nose, mouth
        # left eye indices (approx)
        # NOTE: These indices are approximate; for production map correctly
        def denorm(idx):
            l = face_landmarks[idx]
            return (int(l.x * img_w), int(l.y * img_h))

        try:
            # blink: check EAR
            if current_prompt == 'blink':
                left_eye = [denorm(i) for i in [33, 160, 158, 133, 153, 144]]
                right_eye = [denorm(i) for i in [362, 385, 387, 263, 373, 380]]
                ear_l = eye_aspect_ratio(left_eye)
                ear_r = eye_aspect_ratio(right_eye)
                ear = (ear_l + ear_r) / 2.0
                # if eye closed recently
                if ear < 0.18:
                    self.success = True
                    return True, f'blink detected ear={ear:.3f}'
                else:
                    return False, f'no blink ear={ear:.3f}'

            elif current_prompt == 'smile':
                # mouth landmarks around lips
                mouth_idx = [61, 291, 13, 14, 78, 308, 191, 80]
                mouth = [denorm(i) for i in mouth_idx]
                mar = mouth_aspect_ratio(mouth)
                if mar > 0.35:
                    self.success = True
                    return True, f'smile detected mar={mar:.3f}'
                return False, f'no smile mar={mar:.3f}'

            elif current_prompt in ('turn_left', 'turn_right'):
                # compare nose x relative to face width
                nose = denorm(1)  # tip index approx
                # some heuristics: if nose x is left of face center significantly -> turned left
                # To get face center, use average of some landmarks
                xs = [denorm(i)[0] for i in [10, 152, 234, 454]]
                face_cx = int(np.mean(xs))
                dx = nose[0] - face_cx
                if current_prompt == 'turn_left' and dx < -15:
                    self.success = True
                    return True, f'turn_left detected dx={dx}'
                if current_prompt == 'turn_right' and dx > 15:
                    self.success = True
                    return True, f'turn_right detected dx={dx}'
                return False, f'no turn dx={dx}'

            elif current_prompt == 'nod':
                # use nose y movement compared to start (prev_nose_y)
                nose = denorm(1)
                if prev_nose_y is None:
                    return False, 'no prev for nod'
                dy = nose[1] - prev_nose_y
                if dy > 10:
                    self.success = True
                    return True, f'nod detected dy={dy}'
                return False, f'no nod dy={dy}'

        except Exception as e:
            return False, f'err:{e}'


# ---------------------- Main capture and logic ----------------------

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Camera not opened')
        return

    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1,
                                      refine_landmarks=True,
                                      min_detection_confidence=0.6,
                                      min_tracking_confidence=0.6)

    engine = LivenessEngine(buffer_seconds=3, fps=15)
    ap = ActivePromptEngine(timeout=6)
    prompt = None
    prompt_expires = 0
    prev_nose = None

    # overall decision windows
    passive_scores = deque(maxlen=15)
    active_success = False
    start_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = imutils.resize(frame, width=800)
        img_h, img_w = frame.shape[:2]
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(frame_rgb)
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if results.multi_face_landmarks and len(results.multi_face_landmarks) > 0:
            lm = results.multi_face_landmarks[0].landmark
            # get face rect
            x1, y1, x2, y2 = rect_from_landmarks(lm, img_w, img_h)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)

            # Passive anti-spoof check
            is_spoof, details = engine.is_spoof(frame_gray, frame, (x1, y1, x2, y2))
            passive_scores.append((is_spoof, details))

            # Active prompt handling
            if prompt is None or (time.time() - prompt_expires) > ap.timeout + 1:
                prompt = ap.next_prompt()
                prompt_expires = time.time()

            # check prompt
            nose_idx = 1
            nose = lm[nose_idx]
            nose_xy = (int(nose.x * img_w), int(nose.y * img_h))
            if prev_nose is None:
                prev_nose = nose_xy
            ok, explanation = ap.check(prompt, lm, img_w, img_h, prev_nose[0], prev_nose[1])
            if ok:
                active_success = True
                cv2.putText(frame, f'Active OK: {prompt}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                # reset prompt after success
                prompt = None
                prev_nose = None
            else:
                cv2.putText(frame, f'Prompt: {prompt} ({int(time.time()-ap.start_time)}s)', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 180, 255), 2)
                cv2.putText(frame, f'Check: {explanation}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 180, 255), 2)

            # Passive summarise
            recent = passive_scores[-5:]
            spoof_votes = sum(1 for s, _ in recent if s)
            micro_vals = [d['micro'] for s, d in recent if 'micro' in d]
            avg_micro = np.mean(micro_vals) if micro_vals else 0
            tex_vals = [d['texture'] for s, d in recent if 'texture' in d]
            avg_tex = np.mean(tex_vals) if tex_vals else 0

            cv2.putText(frame, f'Passive micro:{avg_micro:.3f} tex:{avg_tex:.3f} spoof_votes:{spoof_votes}', (10, img_h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (200, 200, 200), 2)

            # Final decision heuristic
            # require: active_success and spoof_votes low and average texture/micro above thresholds
            final_ok = False
            if active_success and spoof_votes <= 1 and avg_micro > 0.15 and avg_tex > 0.32:
                final_ok = True
                cv2.putText(frame, 'KYC PASSED', (img_w - 180, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 3)
            else:
                cv2.putText(frame, 'KYC NOT PASSED', (img_w - 220, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 3)

            # draw landmarks for debugging (optional)
            for i, lmpt in enumerate(lm):
                x, y = int(lmpt.x * img_w), int(lmpt.y * img_h)
                if i % 10 == 0:
                    cv2.circle(frame, (x, y), 1, (0, 255, 255), -1)

        else:
            cv2.putText(frame, 'No face detected', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('Video KYC (prototype)', frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
