def city_country(city, country, population=''):
    """返回一个字符串。"""
    if population:
        message = f"{city.title()}, {country.title()} - population {population}"
    else:
        message = f"{city.title()}, {country.title()}"
    return message
