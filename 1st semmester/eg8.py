
def main():
	first_number = int(input())
	second_number = int(input())
	(bigger, smaller) = check_for_biggest(first_number, second_number)
	number_writer(smaller, bigger)
	

def check_for_biggest(a,b):
	if a >= b:
		return (a,b)
	else:
		return(b,a)

def number_writer(a,b):
	if a != b:
		print(a, end="\t")
		number_writer(a+1,b)
	else:
		print(a, end="\t")
		print("\nThe End")
		
main()
