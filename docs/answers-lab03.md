# Trả lời câu hỏi thảo luận - Lab 03

## 1. Merge base là gì?
- Merge base là commit tổ tiên chung gần nhất (best common ancestor) giữa hai nhánh trong đồ thị commit của Git.
- Khi hòa nhập nhánh (merge), Git dùng thuật toán 3-way merge để so sánh 3 điểm: commit đỉnh nhánh hiện tại, commit đỉnh nhánh được merge, và commit merge base. Nhờ đó Git nhận biết chính xác phần nào đã thay đổi ở mỗi nhánh để tự động hợp nhất hoặc phát hiện xung đột nếu cả hai cùng sửa một vùng mã.

## 2. Vì sao trên nhánh dùng chung (`master`, `release/*`) phải dùng `revert` thay vì `reset`?
- `git reset` dời con trỏ nhánh về quá khứ và xóa bỏ commit khỏi lịch sử nhánh. Khi đã push lên remote, đưa trạng thái `reset` lên bắt buộc phải dùng `--force`, điều này phá hỏng lịch sử của người khác và bị Branch Protection chặn.
- `git revert` tạo một commit mới đảo ngược các thay đổi của commit cũ mà không làm thay đổi các commit trước đó. Nhờ vậy, toàn bộ lịch sử được bảo toàn nguyên vẹn, minh bạch, đảm bảo truy vết kiểm toán và an toàn để áp dụng qua Pull Request.
