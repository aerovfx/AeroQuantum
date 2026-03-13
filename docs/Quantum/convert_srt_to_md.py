#!/usr/bin/env python3
import os
import re
import glob


def extract_title_from_filename(filepath):
    filename = os.path.basename(filepath)
    name_without_ext = os.path.splitext(filename)[0]
    name_without_lang = re.sub(r"\.en$", "", name_without_ext)
    return name_without_lang.replace("_", " ")


def parse_srt_content(srt_content):
    blocks = re.split(r"\n\s*\n", srt_content.strip())
    text_lines = []

    for block in blocks:
        lines = block.strip().split("\n")
        for line in lines:
            line = line.strip()
            if line and not line.isdigit() and "-->" not in line:
                text_lines.append(line)

    return text_lines


def translate_to_vietnamese(text):
    try:
        from deep_translator import GoogleTranslator

        translator = GoogleTranslator(source="en", target="vi")
        result = translator.translate(text)
        return result if result else text
    except Exception as e:
        print(f"  Translation error: {str(e)[:60]}")
        return text


def translate_in_batches(lines, max_chars=4500, batch_size=30):
    translated = []
    batch = []
    batch_len = 0

    for line in lines:
        line_len = len(line)
        if batch_len + line_len > max_chars or len(batch) >= batch_size:
            if batch:
                batch_text = "\n\n".join(batch)
                trans = translate_to_vietnamese(batch_text)
                translated.extend(trans.split("\n\n"))
                batch = []
                batch_len = 0
        batch.append(line)
        batch_len += line_len

    if batch:
        batch_text = "\n\n".join(batch)
        trans = translate_to_vietnamese(batch_text)
        translated.extend(trans.split("\n\n"))

    return translated


def has_md_files(dir_path):
    """Check if directory already has .md files"""
    for root, dirs, files in os.walk(dir_path):
        for f in files:
            if f.endswith(".md"):
                return True
    return False


def get_srt_files(base_dir):
    """Get all .srt files in directory, excluding already converted"""
    patterns = [
        os.path.join(base_dir, "**/*_translated.srt"),
        os.path.join(base_dir, "**/*.en.srt"),
        os.path.join(base_dir, "**/*.srt"),
    ]

    srt_files = []
    for pattern in patterns:
        files = glob.glob(pattern, recursive=True)
        for f in files:
            if f.endswith(".md"):
                continue
            # Check if corresponding md exists
            md_path = (
                f.replace(".en.srt", ".md")
                .replace("_translated.srt", ".md")
                .replace(".srt", ".md")
            )
            if not os.path.exists(md_path):
                if f not in srt_files:
                    srt_files.append(f)

    return srt_files


def process_directory(base_dir):
    srt_files = get_srt_files(base_dir)

    if not srt_files:
        return 0

    print(f"Found {len(srt_files)} .srt files in {os.path.basename(base_dir)}")

    for idx, srt_path in enumerate(srt_files):
        try:
            with open(srt_path, "r", encoding="utf-8") as f:
                srt_content = f.read()

            text_lines = parse_srt_content(srt_content)
            translated_lines = translate_in_batches(text_lines)
            translated_content = "\n\n".join(translated_lines)

            title = extract_title_from_filename(srt_path)
            translated_title = translate_to_vietnamese(title)

            final_content = f"# {translated_title}\n\n---\n\n{translated_content}"

            # Determine output path based on file pattern
            if ".en.srt" in srt_path:
                md_path = srt_path.replace(".en.srt", ".md")
            elif "_translated.srt" in srt_path:
                md_path = srt_path.replace("_translated.srt", ".md")
            else:
                md_path = srt_path.replace(".srt", ".md")

            with open(md_path, "w", encoding="utf-8") as f:
                f.write(final_content)

            print(f"[{idx + 1}/{len(srt_files)}] Converted: {md_path}")
        except Exception as e:
            print(f"Error processing {srt_path}: {e}")

    return len(srt_files)


def main():
    base_dir = "/Users/pixibox/AeroAgent/sub/subs"

    total = 0

    # Get all subdirectories sorted
    subdirs = sorted(
        [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    )

    for subdir in subdirs:
        full_path = os.path.join(base_dir, subdir)

        # Skip if already has md files
        if has_md_files(full_path):
            print(f"\n=== Skipping (has .md): {subdir} ===")
            continue

        print(f"\n=== Processing: {subdir} ===")
        count = process_directory(full_path)
        if count > 0:
            print(f"Converted {count} files from {subdir}")
            total += count
        else:
            print(f"No files to convert in {subdir}")

    print(f"\n=== TOTAL: {total} files converted ===")


if __name__ == "__main__":
    main()
