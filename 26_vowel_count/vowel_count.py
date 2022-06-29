def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {"a", "e", "i", "o", "u"}
    vowel_dict = {}
    lower_phrase = phrase.lower()
    for letter in lower_phrase:
        if letter in vowels:
            vowel_dict[letter] = lower_phrase.count(letter)
    return vowel_dict