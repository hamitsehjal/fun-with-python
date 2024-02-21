from city_functions import format_city

def test_city_country_name():
    """Are 'santiago,chile' being formatted properly"""
    formatted_version=format_city('santiago','chile')
    assert formatted_version == "Santiago, Chile"

def test_city_country_name_population():
    """Are 'santiago,chile,population=5000000' being formatted properly"""
    formatted_version=format_city('santiago','chile',50_000_000)
    assert formatted_version == "Santiago, Chile - population 50000000"
