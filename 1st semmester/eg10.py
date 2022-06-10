first = 1
second = 1
howMany = 0
sumOfThem = 0

def fibonacci(howMany):
	global first
	global second
	global sumOfThem
	if howMany == 1:
		return 1
	elif howMany == 2:
		return 1
	for i in range(3,howMany+1):
		sumOfThem = first + second
		first = second
		second = sumOfThem
	
	return sumOfThem
def main():
	howMany = int(input())
	conc = fibonacci(howMany)
	print(conc)

main()
	
