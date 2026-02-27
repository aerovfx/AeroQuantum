# Phần III: Cơ bản về Phương trình Dirac

## Giới thiệu

Xin chào mọi người. Chào mừng trở lại với Khám phá Vật lý Lượng tử. Tôi là Charles Clark.

Trong phần này, chúng ta sẽ bắt đầu nghiên cứu Phương trình Dirac, là phương trình nền tảng của cơ học lượng tử tương đối tính để mô tả electron và các hạt spin-1/2 khác.

## Lịch sử và Nền tảng

Bây giờ chúng ta sẽ bắt đầu giới thiệu về phương trình Dirac. Đây là một phương trình đáng kinh ngạc với những hệ quả không thể tin được, và nó thực sự là bước đầu tiên trên con đường hướng tới cơ học lượng tử tương đối tính, đây là một chủ đề sâu sắc theo đúng nghĩa của nó.

Và vì đây là khá nâng cao đối với một khóa học khảo sát như loại này. Và vậy, cách xử lý của chúng ta sẽ cụ thể nhưng không toàn diện lắm.

Chúng ta sẽ xem xét công trình ban đầu của Dirac, người đầu tiên, chỉ vài năm sau khi phương trình Schrodinger được khám phá, đã quyết định rằng ông sẽ điều tra việc mở rộng các ý tưởng cơ học lượng tử để làm cho chúng nhất quán với lý thuyết tương đối.

Phương trình Schrodinger như bạn thấy là một phương trình không tương đối tính dựa trên mô tả cơ học không tương đối tính do cơ học cổ điển.

Vậy Dirac đã bắt tay vào việc tìm hiểu bản chất của phương trình sóng cho electron dưới dạng tương đối tính.

## Phương trình cho Hạt Tự do

Chúng ta sẽ thảo luận chỉ phương trình cho hạt tự do trong một chiều để đơn giản hóa mọi thứ.

Đây là phương trình Schrodinger cho hạt tự do trong một chiều. Và thật dễ dàng để tìm các nghiệm, các nghiệm về cơ bản là e^(i p·r / ℏ) và sau đó e^(-iωt) với E = ℏω.

Vậy, Dirac muốn tìm một phiên bản tương đối tính của phương trình này, sẽ có đặc điểm rất quan trọng sau đây.

Nó sẽ thuần nhất trong các biến thời gian và không gian. Bạn thấy phương trình không tương đối tính là bậc nhất trong thời gian và bậc hai trong đạo hàm không gian, và bởi vì phép biến đổi Lorentz, một phương trình bất biến hoàn toàn sẽ phải tuyến tính trong không gian và thời gian.

## Tính Bất biến Lorentz

Và cũng có một lý do tại sao bạn muốn có một phương trình tiến hóa dạng này, đó là bạn muốn bảo tồn ý tưởng về hàm sóng. Và bạn muốn hiểu một hàm sóng tiến hóa như thế nào theo thời gian.

Vậy những thành phần duy nhất bạn có là động lượng, tất nhiên là p = ℏ/i d/dx. Điều đó có tính bất biến tương đối tính đúng.

Và sau đó có một yêu cầu, đây là quan hệ tán sắc tương đối tính, mô tả mối quan hệ giữa năng lượng, động lượng và khối lượng của hạt.

Vậy bạn muốn phương trình chuyển động của mình thỏa mãn quan hệ tán sắc tương đối tính này.

## Ma trận Dirac

Có thể nên có một số hạng khác ở đây, và sau đó nếu bạn nhìn vào đây và suy nghĩ, bạn sẽ thấy rằng điều này thỏa mãn các điều kiện của tương đối tính, với điều kiện alpha^2 và beta^2 đều bằng 1 và chúng thỏa mãn quan hệ phản giao hoán.

Bạn có thể thấy tại sao không? Được rồi, bạn có thể thấy rằng alpha và beta không thể chỉ là các số thuần túy. Thực tế, không một trong số chúng có thể là một số thông thường vì quan hệ phản giao hoán phải được thỏa mãn.

Nhưng trong cơ học lượng tử, chúng ta khá quen với việc sử dụng các toán tử tuyến tính, và ví dụ đây là các lựa chọn của alpha và beta, bạn có thể chọn sigma1 và sigma3 cho beta. Đây là các ma trận Pauli và điều này có một diễn giải hình học khá trực tiếp.

Vậy bạn quen với các phép toán không giao hoán. Trong hệ hai chiều, điều này phản ánh vectơ qua đường 45 độ, và sigma 3 ở đây đảo ngược tọa độ.

## Năng lượng Âm và Phản vật chất

Thực tế, phần lớn những gì chúng ta làm bây giờ sẽ không phụ thuộc vào việc chọn một biểu diễn cụ thể cho alpha và beta. Đầu tiên, có nhiều lựa chọn cho kết quả giống nhau và nó không duy nhất, giống như vấn đề hiệu chuẩn và phương sai. Điều quan trọng là chúng thỏa mãn các quan hệ giao hoán.

Nhưng nếu bạn chọn ma trận 2x2, dễ giải quyết, phương trình dừng Dirac chỉ tỉ lệ với sóng phẳng, và điều đáng chú ý là bạn nhận được cả năng lượng dương và năng lượng âm.

Bạn không bao giờ nhận được năng lượng âm trong giải pháp cho hạt tự do trong cơ học không tương đối tính vì điều đó sẽ yêu cầu một động lượng ảo và sẽ tạo ra một hàm sóng không thể chuẩn hóa.

Nhưng như bạn sẽ thấy trong bài tập về nhà, nếu bạn có một nghiệm của phương trình Dirac là năng lượng dương, thì bạn có thể tìm từ đó một nghiệm khác có năng lượng âm.

Và nó có cùng các đặc tính mong muốn của nghiệm năng lượng dương. Không có gì trong toán học nói rằng bạn có thể loại trừ các nghiệm năng lượng âm, như trong phương trình Schrodinger không tương đối tính.

Và những điều này chỉ ra sự tồn tại của phản vật chất, đó là các nghiệm năng lượng âm đã được tìm thấy là liên quan đến sự tồn tại của các phản hạt có mặt cho tất cả các hạt.

## Tổng kết

Như vậy, chúng ta đã xem xét cơ bản về phương trình Dirac, một trong những phương trình quan trọng nhất trong vật lý lượng tử tương đối tính, dẫn đến sự tiên đoán về spin và phản vật chất.
