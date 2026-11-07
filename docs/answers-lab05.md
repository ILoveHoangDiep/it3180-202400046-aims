# Trả lời câu hỏi thảo luận - Lab 05

## 1. Ưu, nhược điểm của mô hình Upstream First so với Release First?
- **Release First (Làm hotfix từ nhánh release cũ rồi cherry-pick về master)**:
  - *Ưu điểm*: Phát hành bản vá khẩn cấp nhanh nhất cho người dùng đang gặp sự cố trên production mà không cần quan tâm đến trạng thái dang dở của `master`.
  - *Nhược điểm*: Dễ bị quên lan truyền bản sửa lỗi về `master` hoặc các nhánh release kế tiếp, dẫn đến hiện tượng "hồi quy lỗi" (regression) ở các phiên bản sau.
- **Upstream First (Sửa trên master trước rồi cherry-pick sang nhánh release)**:
  - *Ưu điểm*: Đảm bảo mã nguồn chính luôn chứa giải pháp chuẩn và đầy đủ nhất; không bao giờ bị sót lỗi khi phát triển các bản phát hành tương lai.
  - *Nhược điểm*: Khi nhánh `master` có kiến trúc đã thay đổi quá nhiều so với bản phát hành cũ, việc cherry-pick ngược về nhánh release sẽ gặp nhiều xung đột (conflict) phức tạp.

## 2. Nếu quên lan truyền bản sửa sang release/lab05, lệnh nào ở Phần F sẽ phát hiện?
- Lệnh **vòng lặp kiểm tra hành vi shell script**:
  ```bash
  for ref in v1.0.1 v1.1.0 master; do ... done
Nếu quên lan truyền, mốc v1.1.0 sẽ in ra kết quả 0 (không tìm thấy do phân biệt hoa/thường), trong khi v1.0.1 và master in ra 1.

Lệnh git log --all --grep "cherry picked from commit <FIX_SHA>": Sẽ chỉ hiển thị 1 commit thay vì 2 commit.
