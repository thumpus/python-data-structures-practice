def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num_string1 = str(num1)
    num_string2 = str(num2)
    dict1 = {}
    dict2 = {}
    for letter in num_string1:
        if letter in dict1.keys():
            dict1[letter] = dict1[letter] + 1
        else:
            dict1[letter] = 1
    for letter in num_string2:
        if letter in dict2.keys():
            dict2[letter] = dict2[letter] + 1
        else:
            dict2[letter] = 1
    if dict1 == dict2:
        return True
    else:
        return False
    
