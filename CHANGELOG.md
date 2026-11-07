# Changelog

Tất cả các thay đổi đáng chú ý của dự án AIMS-mini sẽ được ghi nhận trong tệp này.
Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
và dự án tuân thủ [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-11-07

### Added
- `search_by_category()`: Hỗ trợ tìm kiếm DVD theo thể loại không phân biệt hoa/thường.

## [1.0.1] - 2026-11-07

### Fixed
- Sửa lỗi `search_by_title` không phân biệt hoa/thường (`Refs #20`).

## [1.0.0] - 2026-11-07

### Added
- `Cart.print_cart()`: In danh sách chi tiết các mặt hàng và tổng chi phí trong giỏ hàng.
- `search_by_title()`: Hỗ trợ tìm kiếm đĩa DVD theo tiêu đề.
- `Cart.total_cost_with_discount()`: Tính tổng chi phí sau khi áp dụng phần trăm giảm giá.
- Bổ sung bộ kiểm thử đơn vị (`unittest`) bao phủ các phương thức giỏ hàng.

### Fixed
- Sửa lỗi giỏ hàng chấp nhận đĩa thứ 21 vượt quá ngưỡng giới hạn 20 đĩa (`Fixes #6`).
