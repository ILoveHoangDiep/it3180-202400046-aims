def search_by_title(items, title):
    """Tìm kiếm đĩa theo tiêu đề (có phân biệt hoa/thường)."""
    return [dvd for dvd in items if title in dvd.title]
