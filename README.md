# Vật Lý Học: Từ Nền Tảng Đến Ứng Dụng

## Tổng Quan

Repository này cung cấp một bộ tài liệu học thuật toàn diện về Vật lý học, từ các nguyên lý cơ bản đến các ứng dụng hiện đại. Các tài liệu được biên soạn dựa trên các bài giảng và khóa học vật lý chuyên sâu, bao gồm nội dung về cơ học lượng tử, vật lý tương đối tính, điện học, và nhiều chủ đề khác.

---

## Mục Lục

1. [Giới thiệu](#giới-thiệu)
2. [Cấu trúc Repository](#cấu-trúc-repository)
3. [Nội dung các chuyên đề](#nội-dung-các-chuyên-đề)
4. [Tài liệu Tham khảo](#tài-liệu-tham-khảo)
5. [Cách sử dụng](#cách-sử-dụng)
6. [Giấy phép](#giấy-phép)

---

## Giới thiệu

### Bối cảnh lịch sử

Vật lý học hiện đại được hình thành từ đầu thế kỷ 20, khi các nhà khoa học như **Max Planck**, **Albert Einstein**, **Niels Bohr**, và **Erwin Schrödinger** phát hiện ra rằng vật lý cổ điển không thể giải thích được các hiện tượng ở quy mô nguyên tử và hạ nguyên tử. Những bất thường thực nghiệm như:

- **Bức xạ vật đen** (Black-body radiation)
- **Hiệu ứng quang điện** (Photoelectric effect)
- **Quang phổ phát xạ nguyên tử** (Atomic emission spectra)

đòi hỏi một khung lý thuyết hoàn toàn mới - **Cơ học lượng tử** (Quantum Mechanics).

### Mục tiêu

Repository này nhằm:

- Cung cấp tài liệu học thuật chuẩn cho sinh viên vật lý, kỹ thuật, và khoa học máy tính
- Giải thích các khái niệm phức tạp bằng ngôn ngữ dễ hiểu
- Bao gồm các công thức toán học và minh họa bằng LaTeX
- Liên kết lý thuyết với các ứng dụng thực tế

---

## Cấu trúc Repository

```
AeroQuantum/
├── docs/
│   └── Quantum/
│       ├── Exploring Quantum Physics/        # Vật lý Lượng tử nâng cao
│       ├── Quantum Physics an overview of a weird world (Basics)/  # Cơ bản QM
│       ├── The Complete Physics Course/      # Khóa Vật lý Toàn diện
│       ├── Physics 100 - Electric Force/    # Điện học
│       ├── Physics Ninja - Ohm's Law/      # Mạch điện một chiều
│       ├── Special Relativity/              # Tương đối tính đặc biệt
│       └── Vat_Ly_Luong_Tu_Tong_Quan.md    # Tổng quan VL Lượng tử
├── README.md
└── (các file cấu hình khác)
```

---

## Nội dung các chuyên đề

### 1. Vật Lý Lượng Tử (Quantum Physics)

| Chuyên đề | Mô tả |
|-----------|--------|
| Phương trình Schrödinger | Phương trình cơ bản của cơ học lượng tử |
| Hàm sóng và ý nghĩa xác suất | Giải thích theo Quy tắc Born |
| Dao động tử điều hòa | Lượng tử hóa năng lượng |
| Nguyên tử Hydro | Cấu trúc electron và quang phổ |
| Siêu dẫn | Hiện tượng và lý thuyết BCS |
| Vướng víu lượng tử | Quantum Entanglement |
| Spin và moment từ | Tính chất lượng tử của hạt |

**Công thức cơ bản:**

Phương trình Schrödinger:
$$i\hbar \frac{\partial \psi}{\partial t} = \hat{H}\psi$$

Năng lượng dao động tử:
$$E_n = \hbar\omega\left(n + \frac{1}{2}\right)$$

Nguyên lý bất định Heisenberg:
$$\Delta x \Delta p \geq \frac{\hbar}{2}$$

### 2. Tương Đối Tính Đặc Biệt (Special Relativity)

| Chuyên đề | Mô tả |
|-----------|--------|
| Biến đổi Lorentz | Hệ phương trình không-thời gian |
| Giãn thời gian | Time Dilation |
| Co lại chiều dài | Length Contraction |
| Năng lượng tương đối tính | $E = mc^2$ |
| Hiệu ứng Doppler tương đối | Redshift |

**Công thức cơ bản:**

Biến đổi Lorentz:
$$t' = \gamma\left(t - \frac{vx}{c^2}\right)$$
$$x' = \gamma(x - vt)$$

với $\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$

Năng lượng tương đối tính:
$$E = \gamma mc^2$$

### 3. Điện Học và Từ Học (Electricity & Magnetism)

| Chuyên đề | Mô tả |
|-----------|--------|
| Định luật Coulomb | Lực tương tác điện |
| Điện trường | Field and Potential |
| Định luật Gauss | Gauss's Law |
| Tụ điện | Capacitors |
| Dòng điện | Current and Ohm's Law |
| Định luật Kirchhoff | Circuit Analysis |

**Công thức cơ bản:**

Định luật Coulomb:
$$F = k\frac{q_1 q_2}{r^2}$$

Định luật Ohm:
$$V = IR$$

Định luật Gauss:
$$\oint \vec{E} \cdot d\vec{A} = \frac{Q_{enc}}{\varepsilon_0}$$

### 4. Cơ Học Cổ Điển (Classical Mechanics)

| Chuyên đề | Mô tả |
|-----------|--------|
| Động học | Kinematics |
| Động lực học | Dynamics |
| Dao động | Oscillations |
| Rơi tự do | Free Fall |
| Chuyển động projectile | Projectile Motion |

**Các phương trình động học:**

$$v = v_0 + at$$
$$x = x_0 + v_0 t + \frac{1}{2}at^2$$
$$v^2 = v_0^2 + 2a(x - x_0)$$

---

## Tài liệu Tham Khảo

### Sách giáo khoa chính

1. **Griffiths, D. J.** (2017). *Introduction to Quantum Mechanics* (3rd ed.). Cambridge University Press.

2. **Griffiths, D. J.** (2017). *Introduction to Electrodynamics* (4th ed.). Cambridge University Press.

3. **Sakurai, J. J., & Napolitano, J.** (2017). *Modern Quantum Mechanics* (2nd ed.). Cambridge University Press.

4. **Dirac, P. A. M.** (1981). *The Principles of Quantum Mechanics* (4th ed.). Oxford University Press.

5. **Halliday, D., Resnick, R., & Walker, J.** (2017). *Fundamentals of Physics* (11th ed.). Wiley.

6. **Tipler, P. A., & Mosca, G.** (2008). *Physics for Scientists and Engineers* (6th ed.). W.H. Freeman.

### Tài liệu trực tuyến

7. **MIT OpenCourseWare - Quantum Physics**
   - https://ocw.mit.edu

8. **MIT OpenCourseWare - Electricity and Magnetism**
   - https://ocw.mit.edu

9. **Khan Academy - Physics**
   - https://www.khanacademy.org/science/physics

10. **HyperPhysics**
    - http://hyperphysics.phy-astr.gsu.edu/hbase/

### Bài báo khoa học gốc

11. **Einstein, A.** (1905). "On a Heuristic Point of View about the Creation and Conversion of Light". *Annalen der Physik*, 17, 132-148.

12. **Bohr, N.** (1913). "On the Constitution of Atoms and Molecules". *Philosophical Magazine*, 26(151), 1-25.

13. **Schrödinger, E.** (1926). "Quantisierung als Eigenwertproblem". *Annalen der Physik*, 79, 361-376.

14. **Born, M.** (1926). "Zur Quantenmechanik der Stoßvorgänge". *Zeitschrift für Physik*, 37, 863-867.

15. **Bardeen, J., Cooper, L. N., & Schrieffer, J. R.** (1957). "Theory of Superconductivity". *Physical Review*, 108(5), 1175-1204.

---

## Cách sử dụng

### Yêu cầu

- Trình duyệt web hỗ trợ hiển thị Markdown
- (Tùy chọn) LaTeX viewer để xem công thức toán học

### Hướng dẫn

1. **Tìm kiếm chủ đề**: Sử dụng mục lục để điều hướng đến chuyên đề quan tâm
2. **Đọc tài liệu**: Mỗi file .md chứa nội dung chi tiết với công thức LaTeX
3. **Tham khảo**: Xem phần tài liệu tham khảo để tìm hiểu sâu hơn

### Ví dụ công thức LaTeX

```latex
$$E = \hbar\omega\left(n + \frac{1}{2}\right)$$
```

Hiển thị:
$$E = \hbar\omega\left(n + \frac{1}{2}\right)$$

---

## Đóng góp

Để đóng góp vào repository này:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/tên-feature`)
3. Commit thay đổi (`git commit -m 'Mô tả thay đổi'`)
4. Push lên branch (`git push origin feature/tên-feature`)
5. Tạo Pull Request

---

## Giấy phép

Repository này được phát hành theo giấy phép **MIT License**.

Bạn được phép:
- Sử dụng cho mục đích cá nhân và thương mại
- Sửa đổi
- Phân phối
- Sử dụng trong sản phẩm thương mại

**Tuy nhiên**, vui lòng ghi nguồn khi sử dụng cho mục đích học thuật.

---

## Trích dẫn

Nếu bạn sử dụng tài liệu này trong công trình nghiên cứu, vui lòng trích dẫn:

```bibtex
@misc{aeroquantum2026,
  author = {AeroQuantum Team},
  title = {Vật Lý Học: Từ Nền Tảng Đến Ứng Dụng},
  year = {2026},
  publisher = {AeroQuantum},
  howpublished = {\url{https://github.com/aeroquantum/docs}},
  note = {Tài liệu học thuật về vật lý học}
}
```

---

## Ghi chú cuối

> *"Nếu bạn nghĩ bạn hiểu cơ học lượng tử, thì bạn không hiểu cơ học lượng tử."*
> — **Richard Feynman**

Vật lý học không chỉ là một lý thuyết vật lý - đó là một ngôn ngữ toán học mô tả thực tại ở quy mô cơ bản nhất của nó. Từ các hạt cơ bản đến vũ trụ vĩ mô, vật lý giúp chúng ta hiểu được bản chất của thế giới xung quanh.

---

**Cập nhật lần cuối**: Tháng 2, 2026
