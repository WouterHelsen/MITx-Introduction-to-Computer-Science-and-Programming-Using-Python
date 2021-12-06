"""
Check if string is a Palindrome in two steps:
- clean up string
-recursive algorithm
"""
def main():
    string = input("What word or sentence would you like to check if it is a palindrome: ")
    if is_palindrome(string):
        print("Yes,", string, "is a palindrome!")
    else :
        print("Not a palindrome!")

def is_palindrome(s):
    def set_char(s):
        s = s.lower()
        clean = ''
        for char in s:
            if char in "abcdefghhijklmnopqrstuvwxyz":
                clean += char
        return clean

    def test_palindrome(s):
        if len(s) <= 1 :
            return True
        else :
            return s[0] == s[-1] and test_palindrome(s[1:-1])

    return test_palindrome(set_char(s))

if __name__ == '__main__':
    main()