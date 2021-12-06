def main():
    char = input("What character are we looking for? ")
    aStr = 'abcdefghijklmno'
    if isIn(char, aStr):
        print("YES")
    else :
        print("NO")

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    middel = int(len(aStr) / 2)

    if char == aStr[middel] or len(aStr) == 1:
        return True
    if char < aStr[middel]:
        return isIn(char, aStr[:middel])
    else:
        return isIn(char, aStr[middel:])

if __name__ == '__main__':
    main()