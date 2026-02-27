# Phần II: Nhiễu loạn Đột ngột và Quantum Quench

## Giới thiệu

Trong video này, tôi sẽ nói về có lẽ loại bài toán đơn giản nhất trong cơ học lượng tử phụ thuộc thời gian, đó là vấn đề nhiễu loạn đột ngột, xảy ra khi thế trong bài toán lượng tử thay đổi rất nhanh so với tất cả các thời gian khác liên quan trong bài toán.

Một thuật ngữ khác cho sự thay đổi đột ngột như vậy trong thế là quantum quench.

## Ví dụ về Quantum Quench

Điều này có thể xảy ra, ví dụ, nếu chúng ta có một thế thay đổi rất nhanh từ một dạng sang dạng khác. Hãy tưởng tượng chúng ta có một dao động tử harmonic, và giả sử ở thời điểm t < 0, hạt ở trạng thái dừng được mô tả bởi hàm sóng Gaussian thông thường, là hàm riêng của trạng thái cơ bản của dao động tử harmonic. Và hãy tưởng tượng tại t = 0, tần số của thế dao động tử harmonic thay đổi nhanh chóng. Nó tăng nhanh đến mức trở thành một thế hoàn toàn khác.

Điều gì xảy ra? Trước khi hỏi câu hỏi, hãy xem điều gì đang xảy ra ở đây.

## Nguyên lý Chính

Hiểu biết chính trong bài toán này là trong khi thế thay đổi rất nhanh, hàm sóng không có thời gian để thay đổi. Vậy hàm sóng ngay trước quench bằng chính xác hàm sóng ngay sau quench, trong xấp xỉ của một quench vô cùng nhanh hoặc vô cùng đột ngột.

Một hiểu biết quan trọng khác là trạng thái lượng tử từng là trạng thái cơ bản ổn định giờ không còn là trị riêng của thế mới.

Hàm sóng cũ chỉ là một số hàm sóng từ quan điểm của Hamiltonian mới. Chúng ta có thể khai triển hàm sóng này theo các hàm riêng của Hamiltonian mới.

## Hiệu ứng trên Hệ nhiều Hạt

Một minh họa thú vị về hiện tượng vật lý có liên quan có thể được thảo luận trong bối cảnh này. Hãy tưởng tượng chúng ta có nhiều hạt ở trạng thái cơ bản. Điều này về cơ bản có nghĩa là có một ngưng tụ Bose-Einstein. Và nếu chúng ta thay đổi tần số của bẫy như tôi vừa cho bạn thấy, điều gì xảy ra là những hạt này từng ở trạng thái cơ bản của thế cũ bây giờ được phân phối lại về cơ bản đến tất cả các trạng thái có thể của thế mới.

Và sau khi thời gian trôi qua, có một số quá trình thư giãn xảy ra, và hệ thống thư giãn đến trạng thái mới, nhưng bây giờ nhiệt độ của trạng thái sẽ lớn hơn. Nhiệt độ thực sự là thước đo năng lượng điển hình của hạt trong hệ nhiều hạt.

Về cơ bản điều tôi đang nói ở đây là bất kỳ sự thay đổi nào trong thế, trong trường hợp này là dao động tử harmonic, nhưng là một khẳng định hoàn toàn chung, bất kỳ sự thay đổi đột ngột nào của thế luôn làm nó nóng lên.

## Ví dụ: Nguyên tử nhận một cú đá

Bây giờ, hãy để tôi chuyển đến một bài toán tương tự nhưng vật lý khác biệt, cũng liên quan đến nhiễu loạn đột ngột nhưng là một nhiễu loạn của một loại hoàn toàn khác.

Bài toán mô hình mà chúng ta sẽ giải thực ra là một bài toán nghiên cứu nghiêm túc cách đây 70 năm trong vật lý lý thuyết. Và nó được xem xét bởi một nhà lý thuyết Nga nổi tiếng chủ yếu làm việc trong vật lý hạt nhân, Arkady Migdal, vào năm 1939.

Và bài toán này cũng xuất hiện trong khóa học Landau-Lifshitz về vật lý lý thuyết cho những ai có quyền truy cập vào tài liệu này.

## Bài toán: Nguyên tử Hydrogen chuyển động

Hãy nêu bài toán. Giả sử chúng ta có một nguyên tử. Để đơn giản, tôi sẽ nói về nguyên tử hydrogen. Nhưng về nguyên tắc chúng ta có thể xem xét bất kỳ nguyên tử nào, bao gồm cả nguyên tử nặng.

Và hãy tưởng tượng một hạt nhân của nguyên tử này, có electron hoặc các electron ở trạng thái cơ bản, nhận được một xung sắc nét cho nó một vận tốc v.

Chúng ta đá nó bằng bức xạ hoặc búa, hoặc chúng ta thả nó từ máy bay, hoặc bất cứ điều gì bạn muốn nghĩ về.

Và điều chúng ta muốn biết là điều gì sẽ xảy ra với electron?

Về cơ bản ở đây nhiễu loạn đột ngột sắc nét là ban đầu chúng ta có nguyên tử đứng yên. Và vào một thời điểm nhất định, hãy nói t = 0, nguyên tử bắt đầu di chuyển với một vận tốc nhất định. Và khi nó làm như vậy, chúng ta muốn theo dõi nó, và chúng ta muốn xem liệu electron có bị kích thích không.

## Tính Xác suất Kích thích

Xác suất kích thích được tính bằng công thức: $$P_{exc} = 1 - \left|\int \psi_0^* \tilde{\psi}_0 dV\right|^2$$

Trong đó ψ0 là hàm sóng ban đầu và ψ̃0 là hàm sóng của trạng thái cơ bản trong hệ quy chiếu chuyển động với hạt nhân.

Kết quả cuối cùng là: $$P_{exc} = 1 - \frac{1}{\left(1 + \frac{mv^2 a_0^2}{4\hbar^2}\right)^4}$$

## Kết luận

Trong cả hai trường hợp, chúng ta đã đối phó với các nhiễu loạn rất sắc nét, rất đột ngột đối với Hamiltonian, và chúng dẫn đến về cơ bản sự phân phối lại năng lượng.
