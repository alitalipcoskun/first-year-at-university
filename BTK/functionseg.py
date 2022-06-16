#1
def writingsOnTheWall(howMany, word):
    i = 0
    while i < howMany:
        print(word)
        i += 1
#2
def converting_to_list(*arg):
    return list(arg)
#3 finding all prime integers between two numbers
def capture_the_primes(a,b):
    prime_list = []
    for i in range(a,b+1):
        for j in range(2,i):
            if i% j == 0:
                break
        else:
            prime_list.append(i)
    return prime_list
#4
def divisible_numbers(integer):
    divisible_numbers_list = []
    for i in range(1,integer):
        if integer % i == 0:
            divisible_numbers_list.append(i)
    
    return divisible_numbers_list

writingsOnTheWall(3, "benmalim")
print(converting_to_list(1,3,5,15,123,1513,31))
print(capture_the_primes(15,71))
print(divisible_numbers(32))

#mapping
def square(number):
    return number**2

list_of_int = [1,2,3,4,5]
result = list(map(square, list_of_int))
result = list(map(lambda x: x**2, list_of_int))
print(result)
result = list(filter(lambda x: x%2 == 0, list_of_int))
print(result)