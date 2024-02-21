def format_city(name,country,population=0):
    """Format the City namee and country"""
    if population == 0:
        formatted_version=f"{name.title()}, {country.title()}"
    else:
        formatted_version=f"{name.title()}, {country.title()} - population {population}"
    return formatted_version


