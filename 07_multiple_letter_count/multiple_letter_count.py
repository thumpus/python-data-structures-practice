def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    count = {}
    for letter in phrase:
        if letter not in count.keys():
            count[letter] =  1
        elif letter in count.keys():
            count[letter] = count[letter] + 1
    return count
            