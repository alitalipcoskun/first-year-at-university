def powering(number):

    def inner(power):
        return number ** power
    
    return inner

#number
two = powering(2)
#power
print(two(3))

five = powering(5)
print(five(3))