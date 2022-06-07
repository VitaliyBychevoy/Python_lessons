def city_country(city, country, population=''):
    if population:
        city_country_ = f"{city}, {country}".title() + f" - population {population}"
    else:
        city_country_ = f"{city}, {country}".title()

    return city_country_