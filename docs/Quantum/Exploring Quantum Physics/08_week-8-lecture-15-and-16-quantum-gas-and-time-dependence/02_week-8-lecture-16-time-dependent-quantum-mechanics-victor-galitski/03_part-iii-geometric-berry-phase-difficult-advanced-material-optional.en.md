# Pha Hình Học Berry

## Giới Thiệu

Trong video này, chúng ta sẽ thảo luận về một lớp hiện tượng lượng tử rất thú vị xuất hiện khi có các nhiễu loạn phụ thuộc thời gian chậm hoặc gọi là adiabatic.

Và các nhiễu loạn adiabatic này tạo ra một cấu trúc toán học rất thanh lịch và đặc biệt là cái được gọi là Pha Hình Học Berry mà chúng ta sẽ suy ra.

Pha Berry được Sir Michael Berry khám phá lý thuyết trong bài báo xuất bản năm 1984 trong Proceedings of the Royal Society of London.

Đây là một bài viết rất hay và thanh lịch.

## Bài Toán Của Berry

Vấn đề mà Sir Michael Berry xem xét là phương trình Schrödinger với Hamiltonian phụ thuộc thời gian, và ông giả định hai điều.

Ông xem xét nhiễu loạn adiabatic, nghĩa là sự phụ thuộc thời gian trong H(t) được giả định là chậm.

Chúng ta có Hamiltonian thay đổi rất chậm.

Và cũng giả sử Hamiltonian trở về chính nó sau một chu kỳ nhất định T.

Và câu hỏi là điều gì xảy ra với hàm sóng khi chúng ta đến thời điểm T?

## Sự Biến Thiên Tham Số

Hãy tưởng tượng chúng ta có Hamiltonian phụ thuộc vào tham số λ.

Đây có thể là từ trường hoặc các tham số của dao động tử điều hòa.

Tham số λ thay đổi theo thời gian.

Sau một khoảng thời gian T, tham số trở về điểm ban đầu.

Vậy chúng ta có một vòng lặp kín trong không gian tham số.

## Pha Động Lực

Dưới các giả định adiabatic, hệ thống vẫn ở trạng thái cơ bản tức thời.

Điều duy nhất có thể xảy ra là một pha, vì tổng số hạt được bảo toàn.

Chúng ta có thể viết: ψ(t) = e^(iθ(t))|0(t)⟩

Pha θ có thể được suy ra từ phương trình Schrödinger.

Pha đầu tiên được gọi là Pha Động Lực (Dynamical Phase).

## Pha Berry

Tuy nhiên, hóa ra điều này không hoàn toàn đúng và có một bổ sung quan trọng cho pha lượng tử này.

Pha bổ sung này chính xác là Pha Berry.

Pha Berry γ có thể được viết như một tích phân từ 0 đến T.

γ(T) = i∫₀ᵀ ⟨0(t)|∂/∂t|0(t)⟩ dt

## Diễn Giải Hình Học

Để có diễn giải hình học, chúng ta thay đổi biến từ thời gian sang tham số λ.

γ = ∮_C ⟨0(λ)|∇_λ|0(λ)⟩·dλ

Đây là một tích phân kín xung quanh vòng C trong không gian tham số.

Chúng ta có thể định nghĩa: a_μ(λ) = i⟨0|∂_μ|0⟩

Và B = ∇ × a là "từ trường giả" trong không gian tham số.

γ = ∮_C a·dλ = ∫_S B·dS

Pha Berry là thông lượng của từ trường giả này qua vùng được bao bởi vòng lặp.

## Ý Nghĩa Vật Lý

Pha Berry là một khái niệm rất phi trực giác và không tầm thường.

Nó được phát hiện muộn trong lịch sử cơ học lượng tử (năm 1984).

Pha Berry có nhiều ứng dụng vật lý quan trọng, bao gồm:
- Hiệu ứng Aharonov-Bohm
- Chất cách điện tôpô (Topological Insulators)
- Vật lý spin và các hệ lượng tử phức tạp

## Kết Luận

Không giống như từ trường trong không gian thực không có nguồn hoặc bồn (không có đơn cực từ), từ trường giả này có thể có các nguồn.

Các nguồn này tương ứng với các điểm suy biến trong phổ của bài toán.

Đây là một chủ đề rất thú vị và đang được nghiên cứu tích cực trong vật lý lượng tử hiện đại.

---

*Tài liệu dựa trên khóa học "Exploring Quantum Physics" - University of Maryland*
