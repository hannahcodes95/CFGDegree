def is_palindrome(word):
    try:
        result = word[::-1].lower()
    except TypeError:
        return 'String only'
    else:
        if result == word.lower():
            print('Palindrome')
            return True
        else:
            print('Not a palindrome')
            return False


is_palindrome('Hannah')