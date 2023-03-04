def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    ans = {}
    for letter in phrase:
        if letter in set(ans.keys()):
            ans[letter] += 1
        else:
            ans[letter] = 1
    
    return ans

