def get_formatted_name(first,last,middle=""):
    """Generate a neatly formatted full name"""
    if middle:
        # middle is not empty
        full_name=f"{first} {middle} {last}"
    else:
        # middle is empty
        full_name = f"{first} {last}"
    return full_name.title()


