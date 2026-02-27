# Toán tử Sinh và Hủy

## Giới thiệu

Bây giờ chúng ta tiến hành giải quyết bài toán dao động tử điều hòa lượng tử bằng phương pháp kỹ thuật. Cần lưu ý rằng có nhiều cách tương đương để giải bài toán này, nhưng hôm nay tôi sẽ trình bày một giải pháp hoàn toàn đại số dựa trên các **toán tử sinh và hủy** (creation/annihilation operators).

Như các bạn sẽ thấy, phổ dao động tử và các tính chất của hàm sóng sẽ được suy ra từ việc phân tích các toán tử sinh-hủy và các quan hệ giao hoán của chúng. Chúng ta sẽ không cần viết phương trình Schrödinger dưới dạng phương trình vi phân hay lo lắng quá nhiều về các điều kiện biên. Chính các toán tử và quan hệ giao hoán của chúng sẽ đủ để xác định mọi thứ chúng ta cần biết.

## Bài toán giá trị riêng

Bài toán chúng ta thực sự đang giải quyết là bài toán giá trị riêng cho toán tử Hamilton với thế năng bậc hai tương ứng với dao động tử điều hòa:

$$H\psi = E\psi$$

## Phân tích thứ nguyên

Chỉ có ba đại lượng ba thứ nguyên xuất hiện trong bài toán mà kết quả cuối cùng, đặc biệt là phổ năng lượng, có thể phụ thuộc vào:

- Khối lượng hạt $m$
- Tần số dao động $\omega$
- Hằng số Planck $\hbar$

Có thể xây dựng một tham số duy nhất từ các đại lượng này có thứ nguyên của năng lượng, và tham số đó là $\hbar\omega$:

$$\text{Thứ nguyên: } [\hbar\omega] = \text{energy}$$

Vì vậy, bất kỳ phổ năng lượng nào của chúng ta cũng phải tỷ lệ với $\hbar\omega$.

## Biến đổi Hamilton

Được thúc đẩy bởi điều này, hãy viết Hamilton chia cho $\hbar\omega$:

$$\frac{H}{\hbar\omega} = \frac{m\omega^2 x^2}{2\hbar\omega} + \frac{p^2}{2m\hbar\omega}$$

Bước tiếp theo là viết lại các số hạng dưới dạng bình phương:

$$\frac{m\omega^2 x^2}{2\hbar\omega} = \left(\sqrt{\frac{m\omega}{2\hbar}}x\right)^2$$

$$\frac{p^2}{2m\hbar\omega} = \left(\frac{p}{\sqrt{2m\hbar\omega}}\right)^2$$

Lý do tôi viết theo cách này là vì tôi muốn sử dụng một công thức tương tự từ giải tích sơ cấp. Cụ thể, nếu chúng ta có hai biến $A$ và $B$, chúng ta có thể viết:

$$A^2 + B^2 = (A - iB)(A + iB)$$

Trong biểu thức này, tôi sẽ liên kết số hạng thứ nhất với $A$ và số hạng thứ hai với $B$. Vì vậy, tôi sẽ viết Hamilton chia cho $\hbar\omega$ dưới dạng:

$$\frac{H}{\hbar\omega} = \left(\sqrt{\frac{m\omega}{2\hbar}}x - \frac{i p}{\sqrt{2m\hbar\omega}}\right)\left(\sqrt{\frac{m\omega}{2\hbar}}x + \frac{i p}{\sqrt{2m\hbar\omega}}\right)$$

## Sửa lỗi và bổ sung

Ở giai đoạn này, tôi phải thừa nhận rằng tôi đã gian lận nghiêm trọng trong phép biến đổi này và phương trình này chứa một lỗi. Thực tế, có một số số hạng bị thiếu mà tôi đã bỏ qua. Vấn đề nằm ở chỗ các đối tượng xuất hiện trong bài toán cơ học lượng tử của chúng ta không chỉ là các biến số - chúng là các **toán tử**.

Cụ thể, đối với các toán tử $x$ và $p$, thứ tự xuất hiện trong phương trình thực sự quan trọng. $x \times p \neq p \times x$, hay nói cách khác, các phép toán này **không giao hoán**.

Nếu chúng ta cố gắng suy lại đẳng thức này cho các toán tử, chúng ta sẽ thấy các số hạng chéo xuất hiện. Và do đó, có một số bổ sung vào biểu thức này:

$$(A - iB)(A + iB) = A^2 + B^2 + \frac{i}{2\hbar}[A, B]$$

Trong đó số hạng bị thiếu là:

$$-\frac{i}{2\hbar}[x, p]$$

và:

$$[x, p] = xp - px$$

Bạn có thể xác minh số hạng này thực sự xuất hiện bằng cách khai triển tích này từng số hạng một và đảm bảo rằng chúng ta đã tái tạo đúng Hamilton ở vế trái.

## Toán tử sinh và hủy

Một điều khác mà chúng ta có thể xác minh bằng cách nhìn vào biểu thức này là dấu ngoặc đầu tiên là liên hợp Hermitian của dấu ngoặc thứ hai. Thật vậy, $x$ và $p$ là các toán tử vật lý và vì vậy chúng là các toán tử Hermitian. Theo định nghĩa: $x^\dagger = x$ và $p^\dagger = p$.

Vì vậy, nếu tôi lấy liên hợp Hermitian của dấu ngoặc thứ hai, $x$ vẫn là $x$, $p$ vẫn là $p$, tất cả các hằng số ở đây là thực và điều duy nhất xảy ra là $i$ sẽ trở thành $-i$, vì vậy chúng ta sẽ tạo ra dấu ngoặc đầu tiên trong biểu thức này.

Dựa trên thực tế này, hãy để tôi giới thiệu một toán tử mới - chúng ta sẽ gọi dấu ngoặc thứ hai là **toán tử $a$**. Và dấu ngoặc đầu tiên sẽ là liên hợp Hermitian của nó, do đó là **$a^\dagger$**.

Và tiến thêm một bước, tôi muốn nói rằng các toán tử này được gọi là toán tử **sinh** (creation) và **hủy** (annihilation). Và phần thảo luận và phép biến đổi tiếp theo sẽ chứa một chứng minh rằng các toán tử này thực sự xứng đáng với tên gọi của chúng.

## Phổ năng lượng

Để giải thích lý do behind thuật ngữ này ngay lập tức, hãy để tôi quảng cáo kết quả chính trước khi chúng ta thực sự suy ra nó.

Kết quả chính ở đây là phổ năng lượng của dao động tử điều hòa, mà như chúng ta sẽ thấy, chứa một chuỗi các mức năng lượng cách đều nhau - các mức năng lượng sao cho bất kỳ cặp lân cận nào của các mức đều cách nhau bởi cùng một năng lượng. Và năng lượng này hóa ra là $\hbar\omega$, chính xác thang năng lượng chúng ta đã thảo luận trước đó.

Và năng lượng của trạng thái cơ bản, trạng thái năng lượng thấp nhất, là $\frac{\hbar\omega}{2}$. Và nhân tiện, $\frac{\hbar\omega}{2}$ này đến chính xác từ số hạng bổ sung mà chúng ta có trong đẳng thức này.

## Ý nghĩa vật lý

Vậy tầm quan trọng của các toán tử sinh-hủy như sau:

Nếu chúng ta chuẩn bị dao động tử lượng tử của chúng ta ở trạng thái cơ bản, và nếu chúng ta áp dụng toán tử sinh $a^\dagger$, nó sẽ tạo ra một lượng tử năng lượng $\hbar\omega$ bằng cách đẩy dao động tử từ trạng thái cơ bản lên trạng thái kích thích thứ nhất. Nếu chúng ta áp dụng lại, chúng ta sẽ đi từ trạng thái kích thích thứ nhất đến trạng thái kích thích thứ hai, v.v.

Và bạn có thể đoán rằng tác động của toán tử hủy $a$ ngược lại với nó. Nếu chúng ta có trạng thái lượng tử với $n = 1$, đây là trạng thái kích thích thứ nhất, nhưng nếu chúng ta áp dụng toán tử hủy, chúng ta sẽ quay trở lại trạng thái cơ bản.

Về cơ bản, các toán tử $a$ và $a^\dagger$ di chuyển chúng ta giữa các trạng thái trong cảnh quan năng lượng này.

## Kết luận

Phương pháp toán tử sinh-hủy cung cấp một cách tiếp cận đại số mạnh mẽ để giải bài toán dao động tử điều hòa lượng tử. Thay vì giải phương trình vi phân phức tạp, chúng ta có thể sử dụng các quan hệ giao hoán để suy ra phổ năng lượng và các tính chất của hàm sóng. Trong video tiếp theo, chúng ta sẽ chứng minh tất cả các tuyên bố này, và chứng minh này sẽ phụ thuộc rất cơ bản vào các quan hệ giao hoán khác nhau giữa các toán tử liên quan ở đây.
