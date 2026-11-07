# Trả lời câu hỏi thảo luận - Lab 02

## 1. Vì sao phải đồng bộ `master` trước khi gửi Pull Request?
- **Đảm bảo tính tương thích tích hợp**: Kiểm tra mã nguồn tính năng mới chạy ăn khớp với những cập nhật mới nhất vừa được đưa vào `master` (ví dụ: Dev 2 kiểm tra hàm tìm kiếm với giỏ hàng đã có `print_cart`).
- **Phát hiện và xử lý xung đột sớm**: Cho phép lập trình viên tự giải quyết xung đột (conflict resolution) và chạy kiểm thử an toàn ngay trên máy cục bộ trước khi chuyển cho reviewer.
- **Giữ PR rõ ràng**: Giúp giao diện so sánh PR trên GitHub chỉ hiển thị đúng các commit và thay đổi mới của tính năng, hỗ trợ review nhanh chóng.

## 2. Khi nào không được dùng `rebase`?
- **Quy tắc vàng của Git**: Tuyệt đối không dùng `rebase` trên các nhánh công khai/dùng chung (như `master`, `release/*`, hoặc nhánh tính năng có nhiều người cùng tham gia).
- **Nguyên nhân**: `rebase` tạo ra các commit hoàn toàn mới với mã SHA mới (viết lại lịch sử). Nếu nhánh đã chia sẻ bị rebase sẽ làm sai lệch đồ thị Git của các thành viên khác, gây phân mảnh và xung đột nghiêm trọng khi pull/push.

## 3. Nhánh `feature/*` khác nhánh `topic/*` ra sao?
- `feature/*`: Dùng để phát triển các tính năng nghiệp vụ cụ thể phục vụ trực tiếp người dùng cuối (ví dụ: `feature/cart-print`, `feature/search-by-title`, `feature/discount`).
- `topic/*`: Dùng cho các công việc liên quan đến hạ tầng kỹ thuật, tài liệu, quy trình hoặc cấu hình nội bộ mà không phải tính năng nghiệp vụ (ví dụ: `topic/pr-template`, `topic/use-case-diagram`, `topic/prepare-release-1.0.0`).
