import random

game_value = random.randint(0,101)
how_many_attemps = 5

i = 1
grade = 100
while i <= how_many_attemps:
	user_guess = int(input())
	if user_guess > game_value:
		grade -= 20
		i += 1
		print("Your guess is bigger than the number.")
	elif user_guess < game_value:
		grade -= 20
		i += 1
		print("Your guess is lesser than the number.")
	else:
		print("You got it!")
		break

print(f"Your grade is {grade}.")
