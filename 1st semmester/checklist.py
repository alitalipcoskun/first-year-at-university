if __name__ == '__main__':
    s = input()
    checkIsAlnum = False
    checkIsAlpha = False
    checkIsLower = False
    checkIsUpper = False
    checkIsDigit = False
    for i in range(len(s)):
        if s[i].isalnum():
            checkIsAlnum = True
        if s[i].isalpha():
            checkIsAlpha = True
        if s[i].isdigit():
            print(i)
            checkIsDigit = True
        if s[i].islower():
            checkIsLower = True
        if s[i].isupper():
            checkIsUpper = True
            
    print(checkIsAlnum)
    print(checkIsAlpha)
    print(checkIsDigit)
    print(checkIsLower)
    print(checkIsUpper)