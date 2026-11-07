def search_by_category(items, category):
    """Tìm kiếm đĩa theo thể loại (không phân biệt hoa/thường)."""
    return [dvd for dvd in items if dvd.category and category.lower() in dvd.category.lower()]


def search_by_title(items, title):
    """Tìm kiếm đĩa theo tiêu đề (có phân biệt hoa/thường)."""
    return [dvd for dvd in items if title in dvd.title]
