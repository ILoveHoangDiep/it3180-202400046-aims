# Trả lời câu hỏi thảo luận - Lab 01

## 1. Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
- **Vị trí lưu trữ**: Cấu hình `--global` được lưu tại tệp `~/.gitconfig` trong thư mục Home của người dùng. Cấu hình `--local` được lưu tại `.git/config` bên trong thư mục gốc của repository cụ thể.
- **Khác biệt**: Cấu hình `--global` áp dụng cho mọi kho Git trên máy tính của người dùng nếu kho đó chưa có cấu hình riêng. Cấu hình `--local` chỉ áp dụng riêng cho repository hiện hành và có quyền ưu tiên cao hơn (ghi đè `--global`).

## 2. Vì sao dùng `git mv` thay vì di chuyển tệp thủ công?
- `git mv` thực hiện đồng thời việc di chuyển tệp trên hệ thống tệp và tự động đưa thay đổi vào Staging Area (tương đương chuỗi lệnh di chuyển + `git rm` tệp cũ + `git add` tệp mới).
- Giúp Git nhận diện tường minh trạng thái đổi tên (`renamed`) thay vì báo xóa tệp cũ và tạo một tệp mới không liên quan.
- Bảo toàn tính liên tục của lịch sử commit, cho phép dùng `git log --follow -- <tệp>` để truy vết xuyên suốt qua các lần tái cấu trúc.

## 3. Nhánh `release/lab01` có phải là baseline không?
- **Có**. Theo định nghĩa SCM, Baseline là cấu hình đã được kiểm tra, thống nhất và đóng băng tại một mốc nhất định, chỉ được thay đổi qua quy trình chính thức. Nhánh `release/lab01` (và tag `v0.1.0`) đại diện cho sản phẩm bàn giao hoàn chỉnh của Lab 01, đóng vai trò là mốc chuẩn để đánh giá và làm nền tảng cho các lab tiếp theo.

## 4. Vì sao không commit thẳng vào `master` dù làm một mình?
- Rèn luyện kỷ luật Release Flow chuẩn công nghiệp phần mềm.
- Cách ly các thay đổi đang thử nghiệm sang nhánh riêng (`refactor/*`, `feature/*`), giữ cho nhánh `master` luôn ổn định và có thể chạy được.
- Đảm bảo mọi thay đổi đều được ghi nhận mục đích, diff và kiểm thử qua PR template và checklist nghiệm thu.
- Tuân thủ chính sách bảo vệ nhánh (Branch Protection) trên remote vốn cấm push trực tiếp.
