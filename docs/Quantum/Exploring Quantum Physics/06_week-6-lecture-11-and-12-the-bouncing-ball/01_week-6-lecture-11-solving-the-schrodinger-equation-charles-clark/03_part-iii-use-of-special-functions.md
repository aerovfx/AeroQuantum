# Phần III: Sử dụng Các Hàm Đặc biệt

## Giới thiệu

Xin chào mọi người.

Chào mừng quay lại với khóa học Khám phá Vật lý Lượng tử.

Tôi là Charles Clark.

Bây giờ chúng ta sẽ bắt đầu áp dụng một số công cụ tuyệt vời nhất mà các nhà toán học từng phát triển, các hàm đặc biệt, và

áp dụng chúng để giải các bài toán cơ học lượng tử của các hệ thống đơn giản.

## Thư viện Hàm Toán học Kỹ thuật số

Có nhiều nguồn thông tin tốt về các hàm đặc biệt.

Nhưng thật tốt khi có một tài liệu tham khảo chung để

tất cả mọi người trong khóa học này sẽ sử dụng cùng một tài liệu.

Vậy chúng ta đang sử dụng Thư viện Hàm Toán học Kỹ thuật số,

từ nơi làm việc của tôi,

Viện Tiêu chuẩn và Công nghệ Quốc gia,

nó là một ứng dụng miễn phí,

miễn phí trên toàn thế giới, và

nó chứa thông tin về tất cả các hàm mà chúng ta sẽ sử dụng trong

khóa học này và nhiều hàm khác.

Và còn nhiều điều khác để nói về nó.

Nhưng khi tôi tham chiếu đến một thứ như Hàm Airy,

sẽ được thực hiện trong phần sau của bài giảng này.

Thì điều tôi muốn nói là các biểu diễn cụ thể được cung cấp ở đó.

Mà chúng rất tiêu chuẩn.

Cùng một điều các bạn sẽ tìm thấy trên Wikipedia nhưng

tôi khuyến khích các bạn xem cái này.

## Tài nguyên bổ sung

Một vài tài nguyên khác cho các bạn.

Một khóa học ngắn về toán học.

Điều chắc chắn đáng để xem bởi vì nó cung cấp

được xây dựng bởi Zach Rains và những người cộng sự và cho các bạn một ý tưởng khá tốt

về mức độ điều trị toán học được thực hiện trong khóa học này.

Một hướng dẫn một trang

về các nghiệm đã biết của phương trình Schrödinger

theo các hàm đặc biệt.

Và một chương trình mẫu viết dưới dạng bảng tính

để giải phương trình Schrödinger

bằng tích phân số.

Điều đó là một cái gì đó.

Tôi sẽ không sử dụng cái đó trong phần này,

nhưng là một cái đáng để xem.

Có một cuộc thảo luận ở đó.

Và tôi sẽ cung cấp cho các bạn một số hướng dẫn đơn giản

về cách tích phân số

phương trình Schrödinger trong các trường hợp khi

các bạn đang đối mặt với một bài toán phức tạp

mà không có nghiệm đã biết.

## Schrödinger và Hàm Đặc biệt

Vậy, ai là người đầu tiên sử dụng phương pháp này?

Giải phương trình Schrödinger bằng các hàm đặc biệt?

Không có giải thưởng nào cho việc đoán đúng,

nó thực ra là Schrödinger.

Và các bạn có thể nói rằng công việc đầu tiên của ông,

các bài báo đầu tiên về phương trình sóng

có ảnh hưởng vì một số lý do.

Nhưng một phát triển lâu dài là

nó đã đặt phương trình Schrödinger của

cơ học lượng tử vào một dạng đã được

hiểu rõ trong

cơ học cổ điển

và đó là để quy động

phương trình vi phân

mà các nghiệm có dạng các hàm đã biết vào thời điểm đó.

Vậy những gì Schrödinger đã làm

tất nhiên tầm quan trọng của

công việc của ông tự nó đứng vững.

Ông đã giải thích phổ của nguyên tử hydro,

tính toán các dịch chuyển trong các vạch phổ.

Ông đã phát minh ra lý thuyết nhiễu loạn,

tất cả trong một chuỗi bốn bài báo đáng chú ý.

Nhưng chắc chắn điều rất quan trọng cho

việc triển khai rộng rãi hơn các ý tưởng của ông.

Là ông đã phát triển một khung,

nó ánh xạ đến các bài toán

đã được phát triển tốt

của vật lý toán học cổ điển.

Và chúng ta đang theo cùng một phương pháp ở đây.

## Ba Trường hợp Đơn giản

Vậy trong phần này của bài giảng,

chúng ta sẽ xem xét ba,

chúng ta sẽ bám sát với các ví dụ một chiều, và

chúng ta sẽ xem xét thế năng không đổi,

thế năng tuyến tính, và

tôi đoán, nó sẽ ở phần tiếp theo,

thế năng bậc hai.

Nhưng các bạn có thể nói rằng đây là ba

thế năng đơn giản nhất có thể

về sự phát triển như các đa thức.

Và các nghiệm của phương trình Schrödinger

cho các trường hợp này là hàm mũ cho

thế năng không đổi, Hàm Airy cho thế năng tuyến tính.

Đây là hàm mũ.

Và hàm trụ parabolic

cho bậc hai.

Bây giờ dao động điệu hòa

là một trường hợp đặc biệt của cái đó.

Nhưng chúng ta sẽ đi qua,

chúng ta sẽ đi qua hai trường hợp này và

cố gắng suy ra từ chúng một số nguyên tắc chung

có liên quan cả cho

giải pháp phân tích và số của

phương trình Schrödinger một chiều.

## Thế năng Không đổi

Được rồi, vậy chúng ta hãy bắt đầu với thế năng tuyến tính.

Chúng ta chỉ cần lấy V(x) là một hằng số.

Và đây là phương trình Schrödinger.

Bây giờ, điểm là chúng ta muốn tìm

các nghiệm cho bất kỳ giá trị nào của năng lượng.

Chúng ta muốn tìm một nghiệm tổng quát hợp lệ cho tất cả các năng lượng.

Bởi vì sau đó, với các nghiệm đó trong tay,

chúng ta có thể tìm các nghiệm cụ thể mà

chúng ta cần để thỏa mãn điều kiện biên.

Các bạn sẽ thấy tại sao điều này quan trọng trong một lát.

Nhưng ví dụ, nếu chúng ta chỉ xem xét

một trường hợp trong đó thế năng là

không đổi trên các vùng khác nhau, không đổi

tại các giá trị khác nhau và các vùng khác nhau.

Và các bạn muốn tìm một nghiệm

cho phương trình sóng hợp lệ.

Sẽ là đủ để có thông tin này để các bạn có thể ghép nối,

các bạn có thể khâu

các phần khác nhau lại với nhau.

Phương pháp chúng ta sẽ áp dụng là biến đổi

phương trình Schrödinger ở đây

thành một loại tiêu chuẩn.

Trong trường hợp này,

dạng tiêu chuẩn mà chúng ta thấy

ở đây là Rho là một biến tỷ lệ.

Biến không thứ nguyên.

Và sau đó dấu cộng hoặc trừ liên quan đến việc liệu năng lượng

dương hay âm.

Chúng ta biết rằng năng lượng có thể là bất kỳ số nào trên đường thực nên chúng ta cần tính đến

cả hai trường hợp đó.

## Nghiệm Dao động và Phân rã

Được rồi, chúng ta chỉ cần lấy hệ thống đó.

Chúng ta biến đổi,

chúng ta tìm biến không thứ nguyên

rho là kx, k là vectơ sóng.

Tùy thuộc vào việc năng lượng lớn hơn hay

nhỏ hơn, thế năng,

Giá trị của k được xác định bởi điều đó.

Và vậy có hai loại nghiệm.

Vậy khi e lớn hơn V0,

chúng ta có hai nghiệm độc lập.

Hãy nói lại,

như một phương trình vi phân bậc hai.

Bất kỳ phương trình vi phân bậc hai nào như cái này

có ít nhất hai nghiệm độc lập.

Có nhiều cách khác nhau để chọn chúng nhưng ở đây tôi đã chỉ cho các bạn hai nghiệm độc lập,

sin(rho) và cos(rho).

Chúng ta sẽ nói thêm một chút về sự lựa chọn trong một lát.

Và sau đó trong vùng

nơi e nhỏ hơn V0,

hai nghiệm độc lập có thể được chọn có dạng này,

e mũ rho và e mũ trừ rho.

Vậy bất kỳ nghiệm nào tồn tại trong vùng này

sẽ là một tổ hợp tuyến tính của hai hàm này.

Nhưng điều đó có nghĩa là hành vi chung là phân rã.

Bởi vì nếu các bạn chỉ lấy một lựa chọn ngẫu nhiên của hai hàm này,

thì nghiệm kết quả sẽ phân kỳ khi rho tiến đến vô cùng.

Và trong trường hợp ngoại lệ nơi các bạn chỉ chọn hàm này thì nó phân kỳ

khi rho tiến đến vô cùng.

Bây giờ điều đó có thể được thay đổi bởi

điều kiện biên khác.

Chúng ta phải nhận thức rằng trong điều kiện đặc biệt này,

hành vi chung là phân kỳ.

Vậy điều đó có nghĩa là các bạn có những lựa chọn khó khăn phải được thực hiện.

## Bước Thế và Phản xạ Ánh sáng

Tôi sẽ nói hai điều về phương trình Schrödinger tầm thường này,

mà hoặc có các nghiệm dao động,

hoặc hàm mũ.

Và điều đó là, nếu các bạn có sự hiểu biết chung về các nghiệm,

thì các bạn có thể làm một giải pháp từng phần,

cho một thế thực

tùy ý.

Các bạn có thể xấp xỉ nó trên cơ sở từng phần, và

sau đó bằng cách biết cách giải phương trình trong các vùng thế năng không đổi

các bạn có thể truyền các nghiệm

giữa các vùng khác nhau.

Điều này được sử dụng trong mô hình bán dẫn dị cấu trúc

các vật liệu khoảng trống quang tử cũng được hiểu tốt

về việc có các kỹ thuật để

truyền một hàm sóng qua một vùng không đổi và sau đó khâu

ma trận chuyển tiếp lại với nhau để xem kết quả tổng thể là gì.

Vậy tại sao chúng ta không áp dụng phương pháp đó

cho bài toán đơn giản nhất về giao diện.

Và chúng ta sẽ xem xét một ví dụ mà các bạn thấy mỗi ngày.

Nếu các bạn nhìn qua một cửa sổ,

các bạn thấy sự phản xạ của chính mình.

Tôi muốn nói thậm chí nếu thủy tinh trong suốt

có một số phản xạ và vậy

hóa ra đây là một hiện tượng đó là

một ví dụ về loại hàm bước thế trong cơ học lượng tử.

Vậy chúng ta có V(x) như một hàm của x.

Đây là không khí.

Đây là thủy tinh.

Vậy sự lan truyền của sóng ánh sáng

khi nó đi vào một cửa sổ là tương tự,

rất giống về mặt toán học với bài toán hạt chuyển động trong một thế.

Vậy cách nó được định frame là

chúng ta có ánh sáng

tới từ một khoảng cách lớn của trục âm.

Hàm sóng đó có dạng e mũ ikx.

Sau đó có thành phần phản xạ là một loại

r với hệ số phản xạ nhân e mũ ikx.

Và sau đó hệ số truyền qua ở đây.

Bây giờ làm thế nào để chúng ta xác định

hiệu ứng của thủy tinh đối với ánh sáng?

Hãy để tôi tham khảo câu đố trong dòng.

Vậy khi ánh sáng đi vào thủy tinh,

chiết suất của thủy tinh là khoảng 1.5 có nghĩa là

bước sóng của nó giảm và vậy có nghĩa

phương trình sóng trong vùng bên trong có dạng này.

Và bây giờ rất dễ để xác định hệ số phản xạ.

Vậy những gì chúng ta có, chúng ta có một hàm sóng

trên hai mặt của một giao diện.

Không khí trong thủy tinh.

Vậy chúng ta phải khớp các giá trị của

hàm sóng với các biên.

Vậy cho x = 0 rất dễ,

đó là 1 cộng r ở đây,

t ở đây, vậy

chúng ta phải có 1 cộng r bằng t.

Và sau đó chúng ta khớp các đạo hàm,

đó là phương trình liên tục

được yêu cầu trong cơ học lượng tử.

Một lần nữa dễ dàng để

lấy đạo hàm phía bên này và

đáp án là Ik1 trừ r và

phía bên kia chỉ là ik nhân t.

Và bây giờ chúng ta làm gì?

Chúng ta lấy,

chúng ta lấy phía này.

Chia cho cái kia.

Vậy các bạn thấy, tôi chỉ lấy cái này chia cho cái kia, bằng cái kia chia cho cái này.

Được phương trình đơn giản cho hệ số phản xạ.

Vậy các bạn thấy, vectơ sóng k biến mất cũng như hệ số truyền qua,

và đó dễ dàng để đảo ngược phương trình này để có được điều này, vậy

R = -0.5 trên 2.5 = một phần năm.

Vậy cường độ phản xạ thực tế

r bình phương là 0.04, vậy là 4%.

Điều này khá đúng.

Khi bạn cho ánh sáng qua một cửa sổ, bình thường khoảng

4% bị phản xạ.

Vậy trong phần tiếp theo của bài giảng này

chúng ta sẽ khám phá trình tự tiếp theo của,

trình tự tiếp theo của độ phức tạp, thế năng tuyến tính.
