def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    vowels = {}
    for letter in phrase:
        if letter.lower() in 'aeiou' and letter.lower() in vowels.keys():
            vowels[letter.lower()] += 1
        elif letter.lower() in 'aeiou':
            vowels[letter.lower()] = 1
    
    return vowels