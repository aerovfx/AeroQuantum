# Giới Thiệu về Dao Động Tử Lượng Tử

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ học về việc lượng tử hóa dao động tử cổ điển.

Dao động tử điều hòa là một trong những hệ thống quan trọng nhất trong vật lý lượng tử.

## Dao Động Tử Cổ Điển

Dao động tử cổ điển được mô tả bởi phương trình:

$$m\ddot{x} + kx = 0$$

với tần số góc $\omega = \sqrt{k/m}$.

Năng lượng tổng cộng:

$$E = \frac{p^2}{2m} + \frac{1}{2}kx^2$$

## Lượng Tử Hóa

Trong cơ học lượng tử, năng lượng bị lượng tử hóa:

$$E_n = \hbar\omega\left(n + \frac{1}{2}\right)$$

với $n = 0, 1, 2, 3, ...$

Đây là một trong những kết quả quan trọng nhất của cơ học lượng tử.

## Toán Tử Sinh và Hủy

Chúng ta định nghĩa các toán tử sinh và hủy:

$$a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(x - \frac{i}{m\omega}p\right)$$

$$a = \sqrt{\frac{m\omega}{2\hbar}}\left(x + \frac{i}{m\omega}p\right)$$

Các toán tử này thỏa mãn:

$$[a, a^\dagger] = 1$$

## Hamiltonian

Hamiltonian có thể được viết:

$$H = \hbar\omega\left(a^\dagger a + \frac{1}{2}\right)$$

Trạng thái cơ bản được định nghĩa bởi:

$$a|0\rangle = 0$$

Các trạng thái kích thích:

$$|n\rangle = \frac{(a^\dagger)^n}{\sqrt{n!}}|0\rangle$$

## Hàm Sóng

Hàm sóng của các trạng thái dừng:

$$\psi_n(x) = \frac{1}{\sqrt{2^n n!}}\left(\frac{m\omega}{\pi\hbar}\right)^{1/4} H_n(\xi) e^{-\xi^2/2}$$

với $\xi = \sqrt{\frac{m\omega}{\hbar}}x$ và $H_n$ là đa thức Hermite.

## Kết Luận

Dao động tử điều hòa là hệ thống giải được chính xác và đóng vai trò quan trọng trong nhiều lĩnh vực của vật lý.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
