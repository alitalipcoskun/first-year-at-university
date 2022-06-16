#encapsulation
#def outer(num1):
#    print("outer")
#    def inner_increment(num1):
#        print("inner")
#        return num1+1
#    num2=inner_increment(num1)
#    print(num1,num2)
#
#outer(10)#inner kısmı sadece outer kapsamında çalışır ayrıyeten çagırılamaz.
from logging import exception


def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be integer")
    if not number >= 0:
        raise ValueError("Number must be equal or greater than zero.")

    def inner_factorial(number):
        if number <= 1:
            return 1
        else:
            return number*inner_factorial(number-1)

    return inner_factorial(number)
try:
    inputfile = eval(input())
    print(factorial(inputfile))
except Exception as ex:
    print(ex)
else:
    print("Successful.")
finally:
    print("End of the program.")