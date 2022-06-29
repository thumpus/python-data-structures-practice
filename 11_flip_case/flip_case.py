def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    flipped = ""
    for char in phrase:
        if char.isupper() and char.lower() == to_swap.lower(): 
            flipped = flipped + char.lower()
        elif char.islower() and char == to_swap.lower():
            flipped = flipped + char.upper()
        elif char.lower != to_swap.lower():
            flipped = flipped + char
    return flipped