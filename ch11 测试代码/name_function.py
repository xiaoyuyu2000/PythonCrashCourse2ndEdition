def get_formatted_name(first, last, middle=''):
    """生成整洁的名字。"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
