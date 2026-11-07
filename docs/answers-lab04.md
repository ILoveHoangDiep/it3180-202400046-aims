# Trả lời câu hỏi thảo luận - Lab 04

## 1. Vì sao `release/*` không bao giờ merge ngược vào `master`? So sánh với GitFlow.
- **Lý do không merge ngược**: Nhánh `release/*` là baseline phát hành cố định đã tách ra từ `master`, trong khi `master` liên tục tiến về phía trước để phát triển tính năng mới. Merge ngược cả nhánh release vào `master` có nguy cơ ghi đè cấu hình cũ hoặc gây xung đột diện rộng. Khi cần sửa lỗi (hotfix), ta chỉ bốc tách riêng commit sửa lỗi bằng `git cherry-pick -x` đưa về `master`.
- **So sánh với GitFlow**:
  - *GitFlow*: Duy trì 2 nhánh dài hạn (`main` và `develop`). Nhánh release khi hoàn thành phải merge vào cả hai nhánh này, dễ gây "merge hell".
  - *Release Flow*: Chỉ duy trì duy nhất 1 nhánh chính dài hạn là `master`. Nhánh `release/*` đóng băng baseline và không bao giờ merge ngược vào `master`.

## 2. Vì sao nâng lên phiên bản `1.0.0` mà không phải `0.4.0`?
- Theo Semantic Versioning (SemVer), dải `0.y.z` chỉ dành cho giai đoạn phát triển ban đầu khi API chưa ổn định.
- Tại Lab 04, dự án AIMS-mini đã hoàn thiện cấu trúc gói, giao diện dòng lệnh hoạt động chuẩn xác, có `CHANGELOG.md` chuẩn Keep a Changelog và có bộ kiểm thử `unittest` bao phủ toàn bộ chức năng. Phiên bản `1.0.0` là cam kết chính thức về tính ổn định đầu tiên (First Stable Release) cho người dùng.

## 3. Vì sao công tác chuẩn bị phát hành thực hiện trên `master` trước mà không sửa trên nhánh `release`?
- Nhánh `master` là nguồn chân lý duy nhất (Single Source of Truth).
- Nếu nâng phiên bản và viết `CHANGELOG.md` trên nhánh `release/*`, nhánh `master` sẽ không có những thông tin này, dẫn đến thất lạc lịch sử hoặc gây xung đột khi tạo các nhánh release tiếp theo (`release/lab05`). Chuẩn bị trên `master` trước giúp các nhánh release kế thừa trọn vẹn trạng thái hoàn thiện nhất.
