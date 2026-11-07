def search_by_title(items, title):
    """Tìm kiếm đĩa theo tiêu đề (không phân biệt hoa/thường)."""
    return [dvd for dvd in items if title.lower() in dvd.title.lower()]
