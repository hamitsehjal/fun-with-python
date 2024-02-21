from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    # Call the function 
    formatted_name = get_formatted_name('janis','joplin')
    # Make the assertion
    assert formatted_name == "Janis Joplin"

def test_first_last_midle_name():
    """Do names like 'Gayatri Chikku Sharma' works?"""
    # Call the function
    formatted_name = get_formatted_name('Gayatri','sharma','chicku')
    # assertion
    assert formatted_name == "Gayatri Chicku Sharma"
