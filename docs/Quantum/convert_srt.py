#!/usr/bin/env python3
import os
import re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="en", target="vi")


def parse_srt(content):
    """Parse SRT content and return list of (index, timestamp, text) tuples"""
    blocks = content.strip().split("\n\n")
    results = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) >= 3:
            try:
                index = int(lines[0])
                timestamp = lines[1]
                text = " ".join(lines[2:])
                results.append((index, timestamp, text))
            except:
                continue
    return results


def timestamp_to_markdown(ts):
    """Convert SRT timestamp to markdown format"""
    parts = ts.split(" --> ")
    if len(parts) == 2:
        start = parts[0].replace(",", ".")
        end = parts[1].replace(",", ".")
        return f"### {start} - {end}"
    return ts


def translate_batch(texts, batch_size=15):
    """Translate a batch of texts"""
    translated = []
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        combined = "|||".join(batch)
        try:
            result = translator.translate(combined)
            parts = result.split("|||")
            translated.extend(parts)
        except Exception as e:
            print(f"Batch translation error: {e}")
            translated.extend(batch)
    return translated


def convert_to_vietnamese_markdown(srt_content):
    """Convert SRT content to Vietnamese markdown with timestamps"""
    entries = parse_srt(srt_content)

    texts = [text.strip() for idx, timestamp, text in entries if text.strip()]
    translated_texts = translate_batch(texts)

    md_content = "## Nội dung\n\n"

    trans_idx = 0
    for idx, timestamp, text in entries:
        text = text.strip()
        if not text:
            continue

        ts_markdown = timestamp_to_markdown(timestamp)
        translated_text = (
            translated_texts[trans_idx] if trans_idx < len(translated_texts) else text
        )
        trans_idx += 1

        md_content += ts_markdown + "\n"
        md_content += translated_text + "\n\n"

    return md_content


def generate_md_path(srt_path):
    """Generate the corresponding .md file path"""
    dirname = os.path.dirname(srt_path)
    basename = os.path.basename(srt_path)

    if basename.endswith("_translated.srt"):
        md_name = basename[:-15] + ".md"
    else:
        md_name = basename.replace(".srt", ".md")

    return os.path.join(dirname, md_name)


def process_all_srt(base_dir):
    """Process all _translated.srt files in directory tree"""
    srt_files = []

    for root, dirs, files in os.walk(base_dir):
        for f in files:
            if f.endswith("_translated.srt"):
                srt_files.append(os.path.join(root, f))

    srt_files.sort()

    converted = 0
    skipped = 0

    for srt_path in srt_files:
        md_path = generate_md_path(srt_path)

        if os.path.exists(md_path):
            print(f"SKIP (exists): {os.path.basename(md_path)}")
            skipped += 1
            continue

        print(f"TRANSLATING: {os.path.basename(srt_path)}")

        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()

        md_content = convert_to_vietnamese_markdown(srt_content)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)

        converted += 1
        print(f"  -> Created: {os.path.basename(md_path)}")

    print(f"\n=== Summary ===")
    print(f"Converted: {converted}")
    print(f"Skipped (already exist): {skipped}")
    print(f"Total: {converted + skipped}")


def main():
    base_dir = "/Users/pixibox/AeroAgent/sub/eted/Udemy - Reinforcement Learning for Algorithmic Trading with Python 2024-8"

    print(f"Processing: {base_dir}")
    print("=" * 50)

    process_all_srt(base_dir)

    print("\n=== All conversions completed! ===")


if __name__ == "__main__":
    main()
