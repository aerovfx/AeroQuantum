#!/usr/bin/env python3
import os
import re

base_dir = "/Users/pixibox/AeroAgent/sub/eted/Udemy - Reinforcement Learning beginner to master - AI in Python 2024-11"

srt_files = set()
md_files = set()

for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith("_en.srt"):
            path = os.path.join(root, f)
            basename = os.path.basename(path)
            name_without_ext = basename[:-7]
            md_name = name_without_ext + ".md"
            srt_files.add(md_name)
        elif f.endswith(".md"):
            path = os.path.join(root, f)
            md_files.add(os.path.basename(path))

missing = srt_files - md_files
print(f"Total SRT files: {len(srt_files)}")
print(f"Total MD files: {len(md_files)}")
print(f"Missing MD files: {len(missing)}")
print("\nMissing files:")
for m in sorted(missing):
    print(f"  {m}")
