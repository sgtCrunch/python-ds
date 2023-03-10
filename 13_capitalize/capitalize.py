def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """

    ans = list(phrase)
    ans[0] = ans[0].upper()

    return "".join(ans)