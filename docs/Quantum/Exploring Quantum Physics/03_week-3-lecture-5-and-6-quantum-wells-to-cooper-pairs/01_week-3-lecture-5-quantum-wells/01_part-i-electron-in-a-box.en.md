# Electron Trong Hộp: Bài Toán Giếng Thế Năng

## Giới thiệu

Trong tuần này, chúng ta sẽ quay lại với cơ học lượng tử truyền thống - mô tả bằng phương trình Schrödinger. Hôm nay, tôi sẽ giải phương trình Schrödinger cho một số ví dụ rất quan trọng, nơi chúng ta sẽ thấy cách các thế năng lượng tử có thể giữ các hạt lượng tử dẫn đến các trạng thái liên kết (bound states).

Những ví dụ này sẽ cho chúng ta hiểu biết sâu sắc về các vấn đề phức tạp và thú vị như lý thuyết siêu dẫn. Trong phần cuối của bài giảng hôm nay, chúng ta sẽ thảo luận các giải pháp liên quan đến hiện tượng then chốt gây ra siêu dẫn - đó là các cặp Cooper.

## Phân Loại Thế Năng

### Phương trình Schrödinger

Phương trình Schrödinger có dạng:

$$i\hbar\frac{\partial\psi(\vec{r},t)}{\partial t} = \hat{H}\psi(\vec{r},t)$$

Trong đó Hamiltonian:
$$\hat{H} = \frac{\hat{p}^2}{2m} + V(\vec{r})$$

- Số hạng đầu tiên là động năng
- Số hạng thứ hai là thế năng, phụ thuộc vào bài toán cụ thể

### Hai Loại Thế Năng

1. **Thế hút (Attractive potential)**: Được gọi là **giếng thế năng** (potential wells)
2. **Thế đẩy (Repulsive potential)**: Được gọi là **rào thế năng** (potential barriers)

## Bài Toán Electron Trong Hộp (Electron in a Box)

### Định nghĩa

Bài toán đơn giản nhất là hộp có tường cứng (hard wall boundaries):

- Tại $x = 0$ và $x = L$: Thế năng $V = \infty$ (tường vô hạn)
- Giữa hai điểm này: $V = 0$ (hạt tự do)

Điều này có nghĩa là hạt có thể di chuyển tự do giữa hai bức tường nhưng không thể đi ra ngoài.

### Tương tự Với Dây Đàn Guitar

Hiện tượng lượng tử hóa xuất hiện trong vật lý cổ điển ở nhiều nơi. Ví dụ, dây đàn guitar:

- Dây được cố định tại hai điểm (tương ứng với tường cứng)
- Các bước sóng khả dụng phụ thuộc vào khoảng cách giữa hai điểm

**Bước sóng dài nhất có thể**: $\lambda = 2L$

**Điều kiện biên**: Dao động tại hai đầu bằng không
$$u(0,t) = u(L,t) = 0$$

### Lượng Tử Hóa Bước Sóng

Các bước sóng khả dụng tuân theo:
$$\lambda_n = \frac{2L}{n}, \quad n = 1, 2, 3, \dots$$

Tần số liên hệ với bước sóng qua vận tốc âm thanh.

### Áp Dụng Cho Electron

Trong bài toán lượng tử, tương tự:
- Thay dây đàn bằng electron
- Thay dao động bằng hàm sóng $\psi(x)$

**Điều kiện biên lượng tử**:
$$\psi(0) = \psi(L) = 0$$

Đây là điều kiện nút tại hai đầu - giống như dây đàn.

### Giải Phương Trình Schrödinger

Trong vùng $0 < x < L$, phương trình cho hạt tự do:
$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

Nghiệm có dạng:
$$\psi_n(x) = A\sin\left(\frac{n\pi x}{L}\right)$$

### Năng Lượng Lượng Tử Hóa

Sử dụng quan hệ de Broglie:
$$p = \frac{h}{\lambda} = \frac{n\pi\hbar}{L}$$

Năng lượng động năng:
$$E = \frac{p^2}{2m} = \frac{n^2\pi^2\hbar^2}{2mL^2}$$

**Công thức năng lượng lượng tử hóa:**
$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}, \quad n = 1, 2, 3, \dots$$

### Điểm Quan Trọng

1. **Năng lượng tỷ lệ với $n^2$**: Các mức năng lượng cách nhau không đều
2. **Năng lượng tỷ lệ nghịch với $L^2$**: Hộp càng nhỏ, năng lượng càng cao
3. **Năng lượng cơ bản ($n=1$)**: $E_1 = \frac{\pi^2\hbar^2}{2mL^2} > 0$

### Hàm Sóng Chuẩn Hóa

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$$

Mật độ xác suất:
$$|\psi_n(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)$$

## So Sánh Vật Lý Cổ điển và Lượng Tử

| Vật lý cổ điển | Vật lý lượng tử |
|----------------|-----------------|
| Năng lượng liên tục | Năng lượng rời rạc |
| Hạt có thể có bất kỳ năng lượng nào | Chỉ có các mức năng lượng được phép |
| Vị trí xác định | Vị trí theo xác suất |

## Ứng Dụng

Bài toán electron trong hộp là nền tảng cho:
- Mô hình bán dẫn
- Giếng lượng tử (quantum wells)
- Hộp lượng tử (quantum dots)
- Nguyên tử trong trạng thái liên kết

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
