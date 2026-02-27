# Tích Phân Đường Feynman - Hạt Nhân (Propagator)

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ nghiên cứu hạt nhân (propagator) trong phương pháp tích phân đường Feynman.

Hạt nhân là biên độ xác suất để hạt đi từ điểm này đến điểm khác.

## Định Nghĩa

Hạt nhân được định nghĩa:

$$K(x_f, t_f; x_i, t_i) = \langle x_f, t_f|x_i, t_i \rangle$$

Đây là biên độ xác suất cho quá trình.

## Công Thức Tích Phân Đường

Hạt nhân có thể được viết như tích phân đường:

$$K = \int \mathcal{D}x(t) \exp\left(\frac{i}{\hbar}S[x(t)]\right)$$

trong đó $S[x(t)]$ là hành động.

## Hạt Nhân Cho Hạt Tự Do

Cho hạt tự do, hạt nhân có dạng:

$$K_0(x_f, t_f; x_i, t_i) = \sqrt{\frac{m}{2\pi i\hbar (t_f - t_i)}} \exp\left(\frac{i m (x_f - x_i)^2}{2\hbar (t_f - t_i)}\right)$$

Đây là nghiệm của phương trình Schrödinger cho hạt tự do.

## Hạt Nhân Cho Dao Động Tử

Cho dao động tử điều hòa, hạt nhân phức tạp hơn:

$$K = \sqrt{\frac{m\omega}{2\pi i\hbar \sin(\omega T)}} \exp\left(\frac{i m\omega}{2\hbar \sin(\omega T)}\left((x_f^2 + x_i^2)\cos(\omega T) - 2x_f x_i\right)\right)$$

với $T = t_f - t_i$.

## Ý Nghĩa

Hạt nhân chứa tất cả thông tin về động lực học lượng tử của hệ.

Từ hạt nhân, có thể tính các đại lượng quan tâm.

## Kết Luận

Hạt nhân là khái niệm trung tâm trong phương pháp tích phân đường Feynman.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
