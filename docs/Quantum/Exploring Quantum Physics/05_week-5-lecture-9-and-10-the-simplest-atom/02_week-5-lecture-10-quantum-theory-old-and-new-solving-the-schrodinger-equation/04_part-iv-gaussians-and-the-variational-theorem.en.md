# Gaussian và Định Lý Biến Thiên

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ xem xét phương pháp biến thiên với hàm trial Gaussian.

## Định Lý Biến Thiên

Định lý biến thiên phát biểu rằng:

$$E_0 \leq \frac{\langle\psi|H|\psi\rangle}{\langle\psi|\psi\rangle}$$

trong đó $E_0$ là năng lượng cơ bản thực, và $\psi$ là bất kỳ hàm trial nào.

Đây là phương pháp để ước tính năng lượng cơ bản.

## Hàm Trial Gaussian

Chọn hàm trial có dạng Gaussian:

$$\psi(x) = A e^{-\alpha x^2}$$

với $\alpha$ là tham số biến thiên.

## Tính Toán Năng Lượng

Năng lượng trung bình:

$$\langle E \rangle = \frac{\int_{-\infty}^{\infty}\psi^* H\psi\,dx}{\int_{-\infty}^{\infty}\psi^*\psi\,dx}$$

## Ví Dụ: Dao Động Tử Điều Hòa

Hamiltonian:

$$H = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + \frac{1}{2}m\omega^2 x^2$$

Với hàm trial Gaussian, ta có thể tính $\langle E \rangle$ theo $\alpha$.

Tối thiểu hóa $\langle E \rangle$ theo $\alpha$ cho ta ước tính năng lượng cơ bản.

## Kết Quả

Với phương pháp biến thiên, ta có thể ước tính năng lượng mà không cần giải phương trình Schrödinger chính xác.

Phương pháp này đặc biệt hữu ích cho các hệ phức tạp.

## Kết Luận

Định lý biến thiên và phương pháp trial Gaussian là công cụ mạnh trong vật lý lượng tử.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
