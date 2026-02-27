# Phần I: Giới thiệu về Thế hiệu dụng (Gauge Potentials) và Trường Từ

## Tổng quan

Xin chào các bạn, chào mừng trở lại với khóa học Khám phá Vật lý Lượng tử. Tôi là Charles Clark.

Trong bài giảng này, chúng ta sẽ đi qua một số công cụ thực tế để hiểu và sử dụng mômen động lượng cho các ứng dụng của riêng bạn. Ít nhất khi bạn nhìn vào các bài toán đơn giản.

Và tôi nghĩ những kỹ thuật này sẽ hữu ích cho bạn trong nhiều lĩnh vực khác của vật lý và kỹ thuật.

## Hàm riêng của Mômen Động lượng

Trong các phần thảo luận trước, chúng ta đã tìm thấy rằng bất kỳ hàm thuần nào theo bán kính đều có mômen động lượng bằng không, gần như theo định nghĩa.

Bây giờ, hãy tìm một số hàm có mômen động lượng xác định và không tầm thường.

Chúng ta đã hiểu rõ hệ tọa độ cầu. Vậy còn ba tọa độ Descartes thì sao?

Khi toán tử mômen động lượng tác dụng lên một tọa độ Descartes, nó trả về các tọa độ Descartes khác. Điều này cho thấy rằng khi mômen động lượng tác dụng lên một tọa độ Descartes, nó hoạt động trong một tập đóng. Bất kỳ điều gì nó làm, nó đưa ra một tổ hợp tuyến tính của các tọa độ khác.

Và điều này nhất quán với việc các tọa độ Descartes là các thành viên có mômen động lượng xác định bằng 1, có nghĩa trong cơ học lượng tử rằng giá trị đó trong chúng liên quan đến chuyển động được kết hợp với một tập hợp các tọa độ Descartes đơn lẻ, được liên kết với mômen động lượng bằng hằng số Planck.

Vậy chúng ta đã tìm được một số hàm riêng tiện lợi của mômen động lượng với giá trị bằng 1.

## Quỹ đạo Phân tử

Bây giờ, đây là cách bạn có thể gọi là ứng dụng thực tế: nếu bạn chỉ cần nhân các tọa độ đó với một hàm cầu, bạn sẽ có được một tập hợp tiện lợi các quỹ đạo phân tử.

Đây là những quỹ đạo mà các nhà hóa học thường sử dụng để mô tả liên kết, vì chúng là các quỹ đạo nằm dọc theo một trục cụ thể.

Đây là p1 hoặc px, p2 hoặc py, p3 hoặc pz.

Những thứ này có tính chất rất đơn giản liên quan đến mômen động lượng. Nhưng chúng có thể được định hướng trong không gian theo cách tùy ý.

## Quiz về Mômen Động lượng

Đây là một câu đố khá thú vị để bạn điều tra một số tính chất khác liên quan đến loại linh hoạt này.

Bạn biết những gì khác được xác định bởi vị trí của các trạng thái mômen động lượng nơi bạn muốn chúng ở.

Các tọa độ Descartes này theo nghĩa nào đó có thể được các nhà hóa học sử dụng. Chúng phù hợp để mô tả các mối quan hệ cấu trúc. Nếu bạn có một vòng carbon, bạn có thể sử dụng các quỹ đạo nằm dọc theo các liên kết phân tử.

Nhưng đây là một trường hợp khác. Theo nghĩa nào đó, nó là một tổ hợp tuyến tính khá đơn giản của ba tọa độ đó. Nó chỉ liên quan đến x1 và x2 và x3.

Và đây là ba lựa chọn độc lập. Nhưng những thứ này có một hình chiếu xác định của thành phần thứ ba L3 - thành phần z truyền thống của mômen động lượng - là 1, 0 và -1.

Và chúng thỏa mãn mối quan hệ này.

Toán tử nâng và hạ khi tác dụng lên một trong những toán tử này sẽ thay đổi số lượng từ từ của nó (magnetic quantum number) thêm hoặc trừ 1.

Một tính năng hữu ích của những thứ này là hãy nói chúng ta lấy 1,1 là hàm riêng với m bằng 1, L bằng 1, và m bằng 1.

Và nếu chúng ta chỉ cần nâng nó lên một lũy thừa tùy ý, chúng ta sẽ được một trạng thái với L đơn vị mômen động lượng dọc theo trục l.

Và hóa ra rằng cũng là một hàm riêng của mômen động lượng với giá trị L.

Vậy bằng cách lấy các lũy thừa liên tiếp của hàm này hoặc hàm -1, chúng ta có thể đến giá trị cực đại của m.

Và sau đó, điều đó trở thành giá trị lớn nhất cho một L nhất định.

Và sau đó người ta có thể sử dụng toán tử hạ, ví dụ, để giảm dần và tạo hệ thống tất cả các hàm riêng của bất kỳ giá trị L cụ thể nào.

## Quy trình Xây dựng

Đây là quy trình xây dựng mà tôi vừa đề cập.

Bạn định nghĩa các nguyên hàm (primitives). Bạn sử dụng những thứ đó với mômen động lượng bằng 1 và -1. Và sau đó, ví dụ, chỉ cần lấy tích L lần của giá trị 1 để có trạng thái LL và sau đó sử dụng L trừ. Tác động lên đó để giảm dần, và sau đó chỉ cần lặp lại khi cần thiết để khám phá tất cả các trạng thái của phổ.

Và có lẽ bạn có thể thấy rằng khi bạn làm điều này, về cơ bản bạn đang tạo ra một đa thức lớn trong ba biến x1, x2, x3, và sau đó toán tử trừ L bằng Lx trừ iLy, có nghĩa là Lx hoặc L1 bằng x2p3 trừ x3p2.

Điều đó làm là giữ nguyên bậc của đa thức, nhưng nó chỉ phân phối lại các lũy thừa giữa một số tọa độ Descartes.

Đây là một dấu hiệu nhỏ cho thấy rằng khi bạn vận hành toán tử hạ, bạn không thay đổi bậc của cấu trúc đa thức.

## Ứng dụng của Điều hòa Cầu

Cuối cùng, nếu bạn tìm kiếm cụm từ "điều hòa cầu" trên Google, bạn sẽ thấy chúng được sử dụng trong nhiều ứng dụng đáng chú ý.

Ví dụ, trong xử lý và tổng hợp hình ảnh, và cố gắng tạo ra tính thực tế lớn hơn trong các thuộc tính rõ ràng của ánh sáng phản xạ.

Hóa ra các điều hòa cầu là một cách hiệu quả đáng kinh ngạc để biểu diễn và mã hóa thông tin.

Chúng giống như biến đổi Fourier trên bề mặt của một quả cầu, và trong nhiều trường hợp như chúng ta đã thấy trong một số bài toán cơ học lượng tử này.

Chúng mã hóa thông tin về một quỹ đạo trải rộng khắp không gian một cách rất hiệu quả.
