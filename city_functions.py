def city_country(city, country, population=''):
    """Returns a city and its country"""
    if population:
        full_city = f"{city}, {country} - population {population}"
    else:
        full_city = f"{city}, {country}"
    return full_city.title()
# print(city_country('El Chalten', 'Argentina', 1000))