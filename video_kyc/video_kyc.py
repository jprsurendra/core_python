import cv2
import numpy as np

# ----------------------------
# CONFIG
# ----------------------------
video_path = "input.mp4"          # Input video
watermark_path = "logo.png"       # Watermark (PNG recommended)
output_path = "output.mp4"        # Output video
alpha = 0.3                        # Transparency 0 = invisible, 1 = solid

# ----------------------------
# LOAD VIDEO
# ----------------------------
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    raise Exception("❌ Cannot open video")

fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# ----------------------------
# LOAD WATERMARK
# ----------------------------
wm = cv2.imread(watermark_path, cv2.IMREAD_UNCHANGED)
if wm is None:
    raise Exception("❌ Cannot load watermark image")

# If PNG with alpha → extract alpha channel
if wm.shape[2] == 4:
    b, g, r, a = cv2.split(wm)
    wm_rgb = cv2.merge((b, g, r))
    wm_alpha = a / 255.0
else:
    wm_rgb = wm
    wm_alpha = np.ones(wm_rgb.shape[:2], dtype=float)

# Resize watermark
wm_h, wm_w = wm_rgb.shape[:2]
scale = 0.25
wm_w = int(width * scale)
wm_h = int(wm_h * wm_w / wm_rgb.shape[1])
wm_rgb = cv2.resize(wm_rgb, (wm_w, wm_h))
wm_alpha = cv2.resize(wm_alpha, (wm_w, wm_h))

# ----------------------------
# PROCESS EACH FRAME
# ----------------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Region to blend watermark
    x, y = width - wm_w - 20, height - wm_h - 20
    roi = frame[y:y + wm_h, x:x + wm_w]

    # Blend watermark
    for c in range(3):
        roi[..., c] = (
            roi[..., c] * (1 - wm_alpha * alpha) +
            wm_rgb[..., c] * (wm_alpha * alpha)
        )

    frame[y:y + wm_h, x:x + wm_w] = roi
    out.write(frame)

cap.release()
out.release()
print("✅ Watermark added successfully!")
