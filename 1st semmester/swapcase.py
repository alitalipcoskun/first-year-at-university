def swap_case(s):
    returned_str = ""
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            returned_str = returned_str + chr(ord(i)+ 32)
        elif ord(i) >= 97 and ord(i) <= 122:
            returned_str = returned_str + chr(ord(i)- 32)
        else:
            returned_str = returned_str + chr(ord(i))
        
    return returned_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)