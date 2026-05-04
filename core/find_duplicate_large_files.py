'''
Yes. The best practical approach is to scan your disk, identify large duplicate files, and show them grouped so you can delete extras manually.

Since you use Linux, Python, and likely large project folders, I’ll give you a solid script that:

✅ Recursively scans folders
✅ Finds duplicate files by size + hash
✅ Prioritizes large files first
✅ Ignores permission errors
✅ Shows total recoverable space
✅ Safe (does not delete automatically)

Python Script: Find Duplicate Large Files
'''

import os
import hashlib
from collections import defaultdict

# -------- SETTINGS --------
SCAN_PATH = "/mnt/usb-TOSHIBA_External_USB_3.0_20170530006600F-0:0-part7/"                 # Change path like "/home/ssr"
MIN_FILE_SIZE_MB = 100         # Only files above this size
CHUNK_SIZE = 1024 * 1024 * 10       # 1MB = 1024 * 1024
# --------------------------


def get_file_hash(filepath):
    """Generate SHA256 hash"""
    sha = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(CHUNK_SIZE):
                sha.update(chunk)
        return sha.hexdigest()
    except:
        return None


def human_size(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} PB"


def scan_files(path):
    files_by_size = defaultdict(list)

    print("Scanning files...")

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            try:
                size = os.path.getsize(full_path)

                if size >= MIN_FILE_SIZE_MB * 1024 * 1024:
                    files_by_size[size].append(full_path)

            except:
                continue

    return files_by_size


def find_duplicates(files_by_size):
    duplicates = []

    for size, files in files_by_size.items():
        if len(files) < 2:
            continue

        hash_map = defaultdict(list)

        for file in files:
            file_hash = get_file_hash(file)
            if file_hash:
                hash_map[file_hash].append(file)

        for h, dup_files in hash_map.items():
            if len(dup_files) > 1:
                duplicates.append((size, dup_files))

    return duplicates


def main():
    files_by_size = scan_files(SCAN_PATH)
    duplicates = find_duplicates(files_by_size)

    duplicates.sort(reverse=True, key=lambda x: x[0])

    total_savings = 0

    print("\n===== DUPLICATE LARGE FILES =====\n")

    for idx, (size, files) in enumerate(duplicates, 1):
        wasted = size * (len(files) - 1)
        total_savings += wasted

        print(f"{idx}. Duplicate Group")
        print(f"   File Size : {human_size(size)}")
        print(f"   Copies    : {len(files)}")
        print(f"   Can Save  : {human_size(wasted)}")

        for f in files:
            print("    ", f)

        print("-" * 70)

    print("\nTotal Recoverable Space:", human_size(total_savings))


if __name__ == "__main__":
    main()