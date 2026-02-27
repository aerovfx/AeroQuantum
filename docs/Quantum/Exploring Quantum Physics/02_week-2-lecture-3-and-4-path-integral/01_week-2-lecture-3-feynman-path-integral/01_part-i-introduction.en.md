# Giới Thiệu về Tích Phân Đường Feynman

## Giới Thiệu

Trong bài giảng này, chúng ta sẽ giới thiệu về phương pháp tích phân đường Feynman.

Phương pháp này là một cách tiếp cận khác để xây dựng cơ học lượng tử, dựa trên nguyên lý hành động tối thiểu.

## Từ Cơ Học Cổ Điển Đến Lượng Tử

Trong cơ học cổ điển, một hạt đi từ điểm A đến điểm B theo đường mà tại đó hành động là cực tiểu.

Trong cơ học lượng tử, theo Feynman, hạt đi theo TẤT CẢ các đường có thể từ A đến B.

Mỗi đường đi có một biên độ xác suất, và tổng của tất cả các biên độ này cho ta biên độ xác suất tổng cộng.

## Nguyên Lý Cơ Bản

Nguyên lý cơ bản của tích phân đường:

Mỗi đường đi từ A đến B có một biên độ xác suất exp(iS/ℏ), trong đó S là hành động dọc theo đường đó.

Xác suất để hạt đi từ A đến B bằng bình phương mô-đun của tổng các biên độ.

## Công Thức Tích Phân Đường

Biên độ xác suất tổng cộng:

$$\langle x_f,t_f|x_i,t_i \rangle = \int \mathcal{D}x(t) \exp\left(\frac{i}{\hbar}S[x(t)]\right)$$

Trong đó:
- $\mathcal{D}x(t)$ là phép lấy tích phân trên tất cả các đường đi
- $S[x(t)]$ là hành động dọc theo đường đi

## Hành Động

Hành động cho hạt tự do:

$$S = \int_{t_i}^{t_f} L\,dt = \int_{t_i}^{t_f} \frac{m\dot{x}^2}{2}\,dt$$

Hành động cho hạt trong thế năng:

$$S = \int_{t_i}^{t_f} \left(\frac{m\dot{x}^2}{2} - V(x)\right)\,dt$$

## Liên Hệ Với Phương Trình Schrödinger

Có thể chứng minh rằng tích phân đường Feynman dẫn đến cùng kết quả với phương trình Schrödinger.

Đây là hai cách biểu diễn tương đương của cơ học lượng tử.

## Ý Nghĩa Vật Lý

Tích phân đường cho ta một cách hiểu trực quan về cơ học lượng tử:

- Hạt "thăm" tất cả các đường đi có thể
- Các đường gần đường cổ điển đóng góp nhiều nhất
- Khoảng cách giữa các đường có biên độ dao động nhanh triệt tiêu lẫn nhau

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
