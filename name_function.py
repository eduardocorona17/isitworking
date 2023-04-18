def get_formatted_name(first, last, middle=''):
    """Returns neatly formatted name."""
    if middle:
        full = f"{first} {middle} {last}"
    else:
        full = f"{first} {last}"
    return full.title()
# print(get_formatted_name('Eduardo', 'Yoyo','Corona'))