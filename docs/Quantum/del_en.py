#!/usr/bin/env python3
import os

base_dir = "/Users/pixibox/AeroAgent/sub/eted/Udemy - Reinforcement Learning beginner to master - AI in Python 2024-11"

count = 0
for root, dirs, files in os.walk(base_dir):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                first_line = file.readline().strip()
            if first_line == "## Nội dung":
                os.remove(path)
                count += 1
                print(f"Deleted: {path}")

print(f"\nTotal deleted: {count}")
