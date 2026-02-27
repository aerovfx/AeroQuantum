# Giới Thiệu về Giếng Thế Năng Hữu Hạn

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ nghiên cứu hạt trong giếng thế năng hữu hạn.

Đây là một bước quan trọng từ giếng vô hạn (hộp) sang các hệ thực tế hơn.

## Giếng Thế Năng Hữu Hạn

Giếng thế năng hữu hạn được định nghĩa:

$$V(x) = \begin{cases} 0 & \text{khi } 0 < x < a \\ V_0 & \text{khi } x \leq 0 \text{ hoặc } x \geq a \end{cases}$$

với $V_0 > 0$.

## Phương Trình Schrödinger

Trong các vùng I và III ($x < 0$ và $x > a$):

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V_0\psi = E\psi$$

Trong vùng II ($0 < x < a$):

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

## Nghiệm Của Phương Trình

Trong vùng II (bên trong giếng):

$$\psi_{II}(x) = A\sin(kx) + B\cos(kx)$$

với $k = \sqrt{2mE}/\hbar$.

Trong các vùng I và III (bên ngoài giếng):

$$\psi_{I}(x) = Ce^{-\kappa x}$$

$$\psi_{III}(x) = Fe^{-\kappa x}$$

với $\kappa = \sqrt{2m(V_0 - E)}/\hbar$.

## Điều Kiện Biên

Hàm sóng và đạo hàm của nó phải liên tục tại các điểm $x = 0$ và $x = a$.

## Trạng Thái Liên Kết

Chỉ có các trạng thái với $E < V_0$ (trạng thái liên kết) tồn tại.

Số lượng trạng thái liên kết phụ thuộc vào độ sâu $V_0$ và chiều rộng $a$ của giếng.

## Trạng Thái Liên Tục

Khi $E > V_0$, các hạt có thể di chuyển tự do trong các vùng bên ngoài giếng.

Đây là các trạng thái không liên kết.

## Kết Luận

Giếng thế năng hữu hạn cho ta hiểu biết về:
- Hiệu ứng xuyên hầm (tunneling)
- Cấu trúc vùng năng lượng trong bán dẫn
- Liên kết hóa học

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
