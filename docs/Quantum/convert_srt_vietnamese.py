#!/usr/bin/env python3
import os
import re

# Vietnamese translation dictionary for physics terms
TRANSLATIONS = {
    # Common physics terms
    "relativity": "tương đối",
    "special relativity": "tương đối hẹp",
    "classical physics": "vật lý cổ điển",
    "modern physics": "vật lý hiện đại",
    "reference frame": "hệ quy chiếu",
    "inertial reference frame": "hệ quy chiếu quán tính",
    "time dilation": "giãn thời gian",
    "length contraction": "co lại chiều dài",
    "Lorentz transformation": "biến đổi Lorentz",
    "Galilean transformation": "biến đổi Galile",
    "Galilean invariance": "bất biến Galile",
    "velocity": "vận tốc",
    "momentum": "động lượng",
    "energy": "năng lượng",
    "kinetic energy": "động năng",
    "rest energy": "năng lượng nghỉ",
    "mass": "khối lượng",
    "proper time": "thời gian riêng",
    "space-time": "không-thời gian",
    "Doppler shift": "dịch Doppler",
    "redshift": "dịch đỏ",
    "wave-particle duality": "lưỡng tính sóng-hạt",
    "photon": "photon",
    "electron": "electron",
    "positron": "positron",
    "quantum mechanics": "cơ học lượng tử",
    "speed of light": "tốc độ ánh sáng",
    "constant velocity": "vận tốc không đổi",
    "acceleration": "gia tốc",
    "force": "lực",
    "Newton's laws": "định luật Newton",
    "conservation of momentum": "bảo toàn động lượng",
    "conservation of energy": "bảo toàn năng lượng",
    "mass-energy equivalence": "tương đương khối lượng-năng lượng",
    "experiment": "thí nghiệm",
    "theory": "lý thuyết",
    "hypothesis": "giả thuyết",
    "observation": "quan sát",
    "measurement": "đo lường",
    "frame of reference": "hệ quy chiếu",
    "observer": "người quan sát",
    "event": "sự kiện",
    "simultaneity": "đồng thời",
    "transformation": "biến đổi",
    "invariant": "bất biến",
    "cosmological": "vũ trụ học",
    "radar": "radar",
    "frequency": "tần số",
    "wavelength": "bước sóng",
    "electromagnetic wave": "sóng điện từ",
    "Compton scattering": "tán xạ Compton",
    "de Broglie wavelength": "bước sóng de Broglie",
    "annihilation": "hủy cặp",
    "subatomic particle": "hạt hạ nguyên tử",
    "decay": "phân rã",
    # Common phrases
    "what this basically asserts": "điều cơ bản khẳng định",
    "in other words": "nói cách khác",
    "for example": "ví dụ",
    "in essence": "về bản chất",
    "it follows that": "suy ra",
    "we can conclude": "chúng ta có thể kết luận",
    "this means": "điều này có nghĩa",
    "as a result": "kết quả là",
    "however": "tuy nhiên",
    "therefore": "do đó",
    "consequently": "theo đó",
    "in fact": "thực ra",
    "of course": "tất nhiên",
    "in particular": "đặc biệt",
    "let's see": "hãy xem",
    "consider": "xét",
    "suppose": "giả sử",
    "assume": "thừa nhận",
    "prove": "chứng minh",
    "derive": "suy ra",
    "calculate": "tính toán",
    "determine": "xác định",
    "find": "tìm",
    "show": "chỉ ra",
    "explain": "giải thích",
    "understand": "hiểu",
    "illustrate": "minh họa",
    "demonstrate": "demonstrate",  # Keep English
    "investigate": "khảo sát",
    "explore": "khám phá",
    "analyze": "phân tích",
}


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


def translate_text(text):
    """Simple word/phrase translation for physics content"""
    result = text
    for eng, vie in TRANSLATIONS.items():
        result = re.sub(
            r"\b" + re.escape(eng) + r"\b", vie, result, flags=re.IGNORECASE
        )
    return result


def convert_to_vietnamese_markdown(srt_content, title):
    """Convert SRT content to Vietnamese markdown with LaTeX support"""
    entries = parse_srt(srt_content)

    # Extract chapter info
    chapter_match = re.search(r"(\d+)\.\s*(.+)", title)
    if chapter_match:
        chapter_num = chapter_match.group(1)
        chapter_title = chapter_match.group(2).replace(".srt", "").strip()
    else:
        chapter_num = ""
        chapter_title = title.replace(".srt", "").strip()

    # Translate title
    translated_title = translate_text(chapter_title)

    # Build Vietnamese markdown
    md_content = f"# {translated_title}\n\n"
    md_content += "---\n\n"
    md_content += "## Nội dung chính\n\n"

    # Process entries into coherent sections
    sections = []
    current_section = []

    for idx, timestamp, text in entries:
        text = text.strip()
        if not text:
            continue

        # Translate text
        translated = translate_text(text)
        current_section.append(translated)

        # Break on sentence boundaries or every ~5 entries
        if len(current_section) >= 5 or idx % 5 == 0:
            if current_section:
                sections.append(" ".join(current_section))
                current_section = []

    if current_section:
        sections.append(" ".join(current_section))

    # Write sections with headings
    for i, section in enumerate(sections):
        md_content += f"### Phần {i + 1}\n\n"
        md_content += section + "\n\n"

    # Add LaTeX formula placeholder section if needed
    md_content += "---\n\n"
    md_content += "## Công thức Toán học\n\n"
    md_content += "*Các công thức toán học sẽ được định dạng với ký hiệu LaTeX*\n\n"

    return md_content


def process_directory(dir_path):
    """Process all SRT files in a directory"""
    srt_files = [f for f in os.listdir(dir_path) if f.endswith(".srt")]

    for srt_file in sorted(srt_files):
        srt_path = os.path.join(dir_path, srt_file)
        md_file = srt_file.replace(".srt", ".md")
        md_path = os.path.join(dir_path, md_file)

        print(f"Đang chuyển đổi: {srt_file} -> {md_file}")

        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()

        md_content = convert_to_vietnamese_markdown(srt_content, srt_file)

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)


def main():
    base_dir = "/Users/pixibox/AeroQuantum/docs/Quantum/Special Relativity The Wacky World of Modern Physics"

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
            print(f"\n=== Đang xử lý: {chapter} ===")
            process_directory(chapter_dir)

    print("\n=== Hoàn tất chuyển đổi tất cả các file! ===")


if __name__ == "__main__":
    main()
