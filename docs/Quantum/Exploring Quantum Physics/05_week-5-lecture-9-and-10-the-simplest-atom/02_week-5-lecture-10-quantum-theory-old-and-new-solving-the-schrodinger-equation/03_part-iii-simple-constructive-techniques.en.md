# Kỹ Thuật Xây Dựng Nghiệm Đơn Giản

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ xem xét các kỹ thuật đơn giản để xây dựng nghiệm cho phương trình Schrödinger.

## Phương Pháp Giả Định Nghiệm

Phương pháp đơn giản nhất là giả định dạng của nghiệm và thay vào phương trình Schrödinger.

### Ví Dụ: Hạt Trong Hộp 1D

Giả định nghiệm có dạng:

$$\psi(x) = A\sin(kx) + B\cos(kx)$$

Thay vào phương trình Schrödinger:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

Ta được:

$$\frac{\hbar^2 k^2}{2m}\psi = E\psi$$

Suy ra:

$$E = \frac{\hbar^2 k^2}{2m}$$

## Điều Kiện Biên

Điều kiện biên quyết định các giá trị của k.

Đối với hộp vô hạn ở 0 và a:

$$\psi(0) = 0 \Rightarrow B = 0$$

$$\psi(a) = 0 \Rightarrow \sin(ka) = 0 \Rightarrow k_n = \frac{n\pi}{a}$$

## Nghiệm Hoàn Chỉnh

$$\psi_n(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)$$

$$E_n = \frac{n^2\pi^2\hbar^2}{2ma^2}$$

## Phương Pháp Phân Tích

Một cách tiếp cận khác là phân tích hàm sóng thành các thành phần cơ bản.

## Kết Luận

Các kỹ thuật đơn giản này cung cấp nền tảng cho việc giải các bài toán phức tạp hơn.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
