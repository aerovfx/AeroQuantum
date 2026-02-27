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


def get_title_translations():
    """Return Vietnamese translations for chapter titles"""
    return {
        "Introduction Newtonian Relativity in Classical Physics": "Giới thiệu về Tương đối Newton trong Vật lý Cổ điển",
        "Redefining Our Conception of Space-Time - Part 1 Time Dilation": "Định nghĩa lại Khái niệm Không-Thời gian - Phần 1 Giãn thời gian",
        "Redefining Our Conception of Space-Time - Part 2 Length Contraction": "Định nghĩa lại Khái niệm Không-Thời gian - Phần 2 Co lại chiều dài",
        "The Lorentz Transformation Developing an Absolute Conception of the Universe": "Biến đổi Lorentz - Xây dựng Quan niệm Tuyệt đối về Vũ trụ",
        "Relativistic Doppler Shifts, Radar Systems, and Redshifts": "Dịch Doppler Tương đối, Hệ thống Radar và Dịch đỏ",
        "Relativistic Mechanics - Part 1 Momentum": "Cơ học Tương đối - Phần 1 Động lượng",
        "Relativistic Mechanics - Part 2 Energy": "Cơ học Tương đối - Phần 2 Năng lượng",
        "The Birth of Quantum Mechanics Massless Particles and the True Nature of Light": "Sự ra đời của Cơ học Lượng tử - Hạt Khối lượng bằng không và Bản chất thực sự của Ánh sáng",
    }


def get_video_translations():
    """Return Vietnamese translations for video titles"""
    return {
        "Galilean Invariance & The Galilean Transformation": "Bất biến Galile và Phép biến đổi Galile",
        "The Michelson–Morley Experiment & Problems with the Speed of Light": "Thí nghiệm Michelson-Morley và Vấn đề về Tốc độ Ánh sáng",
        "Example Problems in Newtonian Relativity - Part 1": "Bài tập ví dụ về Tương đối Newton - Phần 1",
        "Example Problems in Newtonian Relativity - Part 2": "Bài tập ví dụ về Tương đối Newton - Phần 2",
        "The Postulates of Special Relativity": "Các Tiên đề của Tương đối Hẹp",
        "Why The Flow of Time is Relative, Not Absolute": "Tại sao Dòng chảy của Thời gian là Tương đối, không phải Tuyệt đối",
        "Time Dilation and Limitations on Speed": "Giãn thời gian và Giới hạn về Tốc độ",
        "Proper Time & the Symmetry of Reference Frames": "Thời gian riêng và Đối xứng của Hệ quy chiếu",
        "Experimental Verification of Time Dilation": "Xác minh Thực nghiệm của Giãn thời gian",
        "Time Dilation Example Problem - Part 1": "Bài tập ví dụ về Giãn thời gian - Phần 1",
        "Time Dilation Example Problem - Part 2": "Bài tập ví dụ về Giãn thời gian - Phần 2",
        "How Time Dilation Implies Length Contraction": "Cách Giãn thời gian Ngụ ý Co lại chiều dài",
        "Experimental Evidence for Length Contraction Decaying Subatomic Particles": "Bằng chứng Thực nghiệm cho Co lại chiều dài - Hạt hạ nguyên tử phân rã",
        "Einstein's Train Paradox - Part 1 Illustrating the Main Dilemma": "Nghịch lý Tàu hỏa của Einstein - Phần 1 Minh họa Khó khăn chính",
        "Eistein's Train Paradox - Part 2 Why the Simultaneity of Events is Relative": "Nghịch lý Tàu hỏa của Einstein - Phần 2 Tại sao Tính đồng thời của Các sự kiện là Tương đối",
        "Deriving the Lorentz Transformation - Part 1 Accounting for Length Contraction": "Suy ra Phép biến đổi Lorentz - Phần 1 Xem xét Co lại chiều dài",
        "Deriving the Lorentz Transformation - Part 2 Accounting for Time Dilation": "Suy ra Phép biến đổi Lorentz - Phần 2 Xem xét Giãn thời gian",
        "Lorentez Transformation Example Problem Revisiting Einstein's Train Paradox": "Bài tập ví dụ về Biến đổi Lorentz - Quay lại Nghịch lý Tàu hỏa của Einstein",
        "Relativistic Velocity Addition Unleashing the Power of Lorentz Transformations": "Cộng vận tốc Tương đối - Khai thác Sức mạnh của Phép biến đổi Lorentz",
        "Relativistic Velocity Addition Example Problems": "Bài tập ví dụ về Cộng vận tốc Tương đối",
        "A Physical Interpretation of the Doppler Shift": "Diễn giải Vật lý của Dịch Doppler",
        "Deriving the Non-Relativistic Doppler Shift Equation": "Suy ra Phương trình Dịch Doppler Phi tương đối",
        "Electromagnetic Waves & the Doppler Shift": "Sóng Điện từ và Dịch Doppler",
        "The Two-Way Doppler Shift & Radar Applications": "Dịch Doppler Hai chiều và Ứng dụng Radar",
        "Investigating Time Dilation's Effect on the Doppler Shift": "Khảo sát Ảnh hưởng của Giãn thời gian lên Dịch Doppler",
        "Deriving the Relativistic Doppler Shift - Electromagnetic Waves Approach": "Suy ra Dịch Doppler Tương đối - Phương pháp Sóng Điện từ",
        "Alternate Derivation of the Relativistic Doppler Shift - Using Lorentz Transform": "Suy ra khác về Dịch Doppler Tương đối - Sử dụng Biến đổi Lorentz",
        "The Relativistc Two-Way Doppler Shift & Relation to Non-Relativistic Results": "Dịch Doppler Hai chiều Tương đối và Mối quan hệ với Kết quả Phi tương đối",
        "Deriving the Relativistic Redshift": "Suy ra Dịch đỏ Tương đối",
        "Why the Redshift Implies an Expanding Universe & the Cosmological Variant": "Tại sao Dịch đỏ Ngụ ý Vũ trụ đang Giãn nở và Biến thể Vũ trụ học",
        "Doppler Shift Example Problem - Part 1 Designing Your Own Doppler Radar Gun": "Bài tập ví dụ về Dịch Doppler - Phần 1 Thiết kế Súng Radar Doppler của riêng bạn",
        "Doppler Shift Example Problem - Part 2 Clutter and Frequency Spectra": "Bài tập ví dụ về Dịch Doppler - Phần 2 Nhiễu và Phổ Tần số",
        "Investigating the Effects of Modified Space-Time on Classical Momentum": "Khảo sát Ảnh hưởng của Không-Thời gian biến đổi lên Động lượng Cổ điển",
        "Why Conservation of Momentum No Longer Holds at High Velocities": "Tại sao Bảo toàn Động lượng không còn Đúng ở Vận tốc cao",
        "Deriving a Candidate Equation for Relativistic Momentum": "Suy ra Phương trình Ứng viên cho Động lượng Tương đối",
        "Verifying the Correct Relativistic Momentum Equation": "Xác minh Phương trình Động lượng Tương đối đúng",
        "Properly Interpretting Relativistic Momentum (Rest Mass vs. Variable Mass)": "Diễn giải đúng Động lượng Tương đối (Khối lượng nghỉ vs Khối lượng biến đổi)",
        "Baking a Revised Formula for Kinetic Energy": "Xây dựng Công thức mới cho Động năng",
        "Unwrapping the Truth of Relativistic Energy": "Khám phá Sự thật về Năng lượng Tương đối",
        "Building Intuition with Rest Energy": "Xây dựng Trực giác với Năng lượng nghỉ",
        "A More Appropriate Measurement for Relativistic Energy The Electron-Volt": "Đo lường Phù hợp hơn cho Năng lượng Tương đối - Electron-volt",
        "Exploring Mass-Energy Equivalence Does Conservation of Mass Still Hold": "Khám phá Tương đương Khối lượng-Năng lượng - Bảo toàn Khối lượng có còn Đúng?",
        "Mass-Energy Equivalence Example Problem": "Bài tập ví dụ về Tương đương Khối lượng-Năng lượng",
        "Deriving the Relativistic Energy-Momentum Relation": "Suy ra Quan hệ Năng lượng-Động lượng Tương đối",
        "Exploring the Implications of the Relativistic Energy-Momentum Relation": "Khám phá Hệ quả của Quan hệ Năng lượng-Động lượng Tương đối",
        "Example Problem #1 Putting the Puzzle Pieces Together to See the Full Picture": "Bài tập ví dụ #1 Ghép các mảnh ghép để xem Bức tranh toàn diện",
        "Example Problem #2 A Spontaneously Decaying Subatomic Particle": "Bài tập ví dụ #2 Hạt hạ nguyên tử phân rã tự phát",
        "Exploring the Plausibility of Massless Particles": "Khảo sát Khả năng của các Hạt không có Khối lượng",
        "Example Problem #1 Electron-Positron Annihilation and PET Scans": "Bài tập ví dụ #1 Hủy cặp Electron-Positron và Chụp cắt lớp PET",
        "Discovering the Wave-Particle Duality of Light The Birth of Quantum Mechanics": "Khám phá Lưỡng tính Sóng-Hạt của Ánh sáng - Sự ra đời của Cơ học Lượng tử",
        "Compton Scattering and the De Broglie Wavelength Why Light has Momentum": "Tán xạ Compton và Bước sóng De Broglie - Tại sao Ánh sáng có Động lượng",
    }


def convert_to_vietnamese_markdown(srt_content, title, chapter_title):
    """Convert SRT content to clean Vietnamese markdown"""
    entries = parse_srt(srt_content)

    # Get Vietnamese title - strip leading number and dot
    video_translations = get_video_translations()
    title_key = re.sub(r"^\d+\.\s*", "", title.replace(".srt", ""))
    translated_title = video_translations.get(title_key, title_key)

    # Build clean Vietnamese markdown
    md_content = f"# {translated_title}\n\n"
    md_content += "---\n\n"
    md_content += f"**Chương:** {chapter_title}\n\n"
    md_content += "---\n\n"
    md_content += "## Tóm tắt nội dung\n\n"
    md_content += "*Nội dung chính được trình bày dưới đây với các thuật ngữ vật lý tương đối tính*\n\n"
    md_content += "---\n\n"
    md_content += "## Nội dung chi tiết\n\n"

    # Combine entries into coherent paragraphs
    paragraphs = []
    current_para = []

    for idx, timestamp, text in entries:
        text = text.strip()
        if not text:
            continue
        current_para.append(text)

        # Create new paragraph every 3-5 entries
        if len(current_para) >= 4:
            paragraphs.append(" ".join(current_para))
            current_para = []

    if current_para:
        paragraphs.append(" ".join(current_para))

    # Write paragraphs with subheadings
    for i, para in enumerate(paragraphs):
        md_content += f"### Đoạn {i + 1}\n\n"
        md_content += para + "\n\n"

    # Add LaTeX section
    md_content += "---\n\n"
    md_content += "## Công thức Toán học\n\n"
    md_content += "```latex\n"
    md_content += "% Các công thức toán học quan trọng trong bài:\n"
    md_content += "% - Phương trình Lorentz\n"
    md_content += "% - Công thức giãn thời gian\n"
    md_content += "% - Công thức co lại chiều dài\n"
    md_content += "% - Công thức động lượng tương đối\n"
    md_content += "% - Công thức năng lượng tương đối\n"
    md_content += "```\n\n"

    # Add reference section
    md_content += "---\n\n"
    md_content += "## Thuật ngữ quan trọng\n\n"
    md_content += (
        "- **Hệ quy chiếu (Reference Frame)**: Hệ tọa độ dùng để mô tả chuyển động\n"
    )
    md_content += "- **Hệ quy chiếu quán tính (Inertial Reference Frame)**: Hệ quy chiếu chuyển động với vận tốc không đổi\n"
    md_content += "- **Thời gian riêng (Proper Time)**: Thời gian đo được trong hệ quy chiếu của đồng hồ\n"
    md_content += "- **Biến đổi Lorentz (Lorentz Transformation)**: Phép biến đổi tọa độ trong không-thời gian tương đối\n\n"

    return md_content


def process_directory(dir_path, chapter_title):
    """Process all SRT files in a directory"""
    srt_files = [f for f in os.listdir(dir_path) if f.endswith(".srt")]
    video_translations = get_video_translations()

    for srt_file in sorted(srt_files):
        srt_path = os.path.join(dir_path, srt_file)
        md_file = srt_file.replace(".srt", ".md")
        md_path = os.path.join(dir_path, md_file)

        print(f"Đang chuyển đổi: {srt_file}")

        with open(srt_path, "r", encoding="utf-8") as f:
            srt_content = f.read()

        md_content = convert_to_vietnamese_markdown(
            srt_content, srt_file, chapter_title
        )

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(md_content)


def main():
    base_dir = "/Users/pixibox/AeroQuantum/docs/Quantum/Special Relativity The Wacky World of Modern Physics"

    chapters = {
        "1. Introduction Newtonian Relativity in Classical Physics": "Giới thiệu về Tương đối Newton trong Vật lý Cổ điển",
        "2. Redefining Our Conception of Space-Time - Part 1 Time Dilation": "Định nghĩa lại Không-Thời gian - Phần 1 Giãn thời gian",
        "3. Redefining Our Conception of Space-Time - Part 2 Length Contraction": "Định nghĩa lại Không-Thời gian - Phần 2 Co lại chiều dài",
        "4. The Lorentz Transformation Developing an Absolute Conception of the Universe": "Biến đổi Lorentz",
        "5. Relativistic Doppler Shifts, Radar Systems, and Redshifts": "Dịch Doppler Tương đối và Radar",
        "6. Relativistic Mechanics - Part 1 Momentum": "Cơ học Tương đối - Động lượng",
        "7. Relativistic Mechanics - Part 2 Energy": "Cơ học Tương đối - Năng lượng",
        "8. The Birth of Quantum Mechanics Massless Particles and the True Nature of Light": "Sự ra đời của Cơ học Lượng tử",
    }

    for chapter_dir, chapter_title in chapters.items():
        full_path = os.path.join(base_dir, chapter_dir)
        if os.path.exists(full_path):
            print(f"\n=== Đang xử lý: {chapter_title} ===")
            process_directory(full_path, chapter_title)

    print("\n=== Hoàn tất! ===")


if __name__ == "__main__":
    main()
