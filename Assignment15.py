
def is_palindrome(s):

    clean = ''.join( c.lower() for c in s if c.isalnum())  #use single quotes to remove space in strings and convert to lowercase

    if len(clean) <= 1:
        return True

    if clean[0] == clean[-1]: #first letter in string and last letter in string
        return is_palindrome(clean[1:-1])

    return False

print(is_palindrome(" A man, a plan, a canal, Panama"))
print(is_palindrome("no 'X' in Nixon"))