def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lower_phrase = phrase.lower()
    title_phrase1 = phrase.replace(lower_phrase[0], lower_phrase[0].upper())
    title_phrase2 = ""
    for i in range(len(title_phrase1)):
        if title_phrase1[i-1] == " ":
            title_phrase2 = title_phrase1.replace(title_phrase1[i], title_phrase1[i].upper())
    return title_phrase2
