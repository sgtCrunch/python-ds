def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 == 1:
        return False

    p = list(parens)
    while len(p) > 0:
        
        if p[0] == ")":
            return False
        else:
            i = p.index(")")
            del p[i]
            del p[0]
            

    
    return True