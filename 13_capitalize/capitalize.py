def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    cap = list(phrase)
    cap[0] = cap[0].upper()
    return ''.join(cap)