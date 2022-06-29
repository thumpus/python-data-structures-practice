def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse = ''
    for i in range(len(phrase)):
        reverse = reverse + phrase[-(i + 1)]
    return reverse

