#!/usr/bin/env python3
import os
import re


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


def convert_to_vietnamese_markdown(srt_content, title):
    """Convert SRT content to Vietnamese markdown"""
    entries = parse_srt(srt_content)

    # Extract chapter number and title
    chapter_match = re.search(r"(\d+)\.\s*(.+)", title)
    if chapter_match:
        chapter_num = chapter_match.group(1)
        chapter_title = chapter_match.group(2).replace(".srt", "")
    else:
        chapter_num = ""
        chapter_title = title.replace(".srt", "")

    # Start building markdown
    md_content = f"# {chapter_title}\n\n"
    md_content += "---\n\n"
    md_content += "## Nội dung\n\n"

    # Group entries by paragraphs (roughly every few entries)
    current_paragraph = []

    for idx, timestamp, text in entries:
        # Clean up the text
        text = text.strip()
        if not text:
            continue

        # Handle mathematical expressions - convert common patterns to LaTeX
        # Note: SRT files typically don't have formulas, but we'll prepare for them

        current_paragraph.append(text)

        # Create a new section roughly every 3-4 entries or on significant pauses
        if len(current_paragraph) >= 4:
            md_content += "###\n\n"
            md_content += " ".join(current_paragraph) + "\n\n"
            current_paragraph = []

    # Add remaining paragraphs
    if current_paragraph:
        md_content += "###\n\n"
        md_content += " ".join(current_paragraph) + "\n\n"

    return md_content


def process_directory(dir_path):
    """Process all SRT files in a directory"""
    srt_files = [f for f in os.listdir(dir_path) if f.endswith(".srt")]

    for srt_file in sorted(srt_files):
        srt_path = os.path.join(dir_path, srt_file)
        md_file = srt_file.replace(".srt", ".md")
        md_path = os.path.join(dir_path, md_file)

        print(f"Converting: {srt_file} -> {md_file}")

        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()

        md_content = convert_to_vietnamese_markdown(srt_content, srt_file)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)


def main():
    base_dir = "/Users/pixibox/AeroQuantum/docs/Quantum/Special Relativity The Wacky World of Modern Physics"

    # Process each chapter directory
    chapters = [
        "1. Introduction Newtonian Relativity in Classical Physics",
        "2. Redefining Our Conception of Space-Time - Part 1 Time Dilation",
        "3. Redefining Our Conception of Space-Time - Part 2 Length Contraction",
        "4. The Lorentz Transformation Developing an Absolute Conception of the Universe",
        "5. Relativistic Doppler Shifts, Radar Systems, and Redshifts",
        "6. Relativistic Mechanics - Part 1 Momentum",
        "7. Relativistic Mechanics - Part 2 Energy",
        "8. The Birth of Quantum Mechanics Massless Particles and the True Nature of Light",
    ]

    for chapter in chapters:
        chapter_dir = os.path.join(base_dir, chapter)
        if os.path.exists(chapter_dir):
            print(f"\n=== Processing: {chapter} ===")
            process_directory(chapter_dir)

    print("\n=== All conversions completed! ===")


if __name__ == "__main__":
    main()
