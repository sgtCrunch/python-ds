def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = [letter for letter in s if letter.lower() in 'aeiou']

    vowels = vowels[::-1]
    ans = []

    for letter in s:
        if letter.lower() in 'aeiou':
            ans.append(vowels[0])
            del vowels[0]
        else:
            ans.append(letter)
    
    return "".join(ans)
