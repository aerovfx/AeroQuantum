# Sóng Dao Động Tử Điều Hòa

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ xem xét các hàm sóng của dao động tử điều hòa.

## Hàm Sóng

Các hàm sóng của dao động tử điều hòa được biểu diễn qua đa thức Hermite.

$$\psi_n(x) = N_n H_n(\xi) e^{-\xi^2/2}$$

với $\xi = \sqrt{\frac{m\omega}{\hbar}}x$.

## Đa Thức Hermite

$$H_0(\xi) = 1$$

$$H_1(\xi) = 2\xi$$

$$H_2(\xi) = 4\xi^2 - 2$$

$$H_n(\xi) = (-1)^n e^{\xi^2}\frac{d^n}{d\xi^n}e^{-\xi^2}$$

## Hệ Số Chuẩn Hóa

$$N_n = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^n n!}}$$

## Tính Chất

- Các hàm sóng trực giao
- Đối xứng: $\psi_n(-x) = (-1)^n \psi_n(x)$
- Số lượng nút = n

## Giá Trị Trung Bình

$$\langle x^2 \rangle_n = \frac{\hbar}{m\omega}\left(n + \frac{1}{2}\right)$$

$$\langle p^2 \rangle_n = m\hbar\omega\left(n + \frac{1}{2}\right)$$

## Kết Luận

Các hàm sóng dao động tử điều hòa có nhiều ứng dụng trong vật lý.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
