menu = "1- Coffee Latte \t$1.75\n2- Americano \t\t$2.00\n3- Cappucino \t\t$1.75\n4- Latte \t\t$3.00\n5- Macchiato \t\t$4.00\n6- Mocha \t\t$1.25\n7- Tea \t\t\t$1.00\n8- Water \t\t$0.50\n9- Hot Chocolate \t$2.00\n10- White Hot Chocolate $2.25\n"
print("Welcome to the vending machine. To continue to the process, please enter money to increase your balance.")
print(menu)
balance = 0
coffeeLatte = 5
americano = 5
cappucino = 5
coolLime = 5
macchiato = 5
mocha = 5
tea = 5
water = 5
hotChocolate = 5
whiteHotChocolate = 5

def productService():
    print("Please select the product number which you want to produce(1 to 10): ")
    productNumber = int(input())
    global balance
    global coffeeLatte
    global americano
    global cappucino
    global coolLime
    global macchiato
    global mocha
    global tea
    global water
    global hotChocolate
    global whiteHotChocolate
    
    if productNumber == 1 and balance >= 1.75 and coffeeLatte > 0:
        coffeeLatte = coffeeLatte - 1
        balance = balance - 1.75
        print("Here is your coffee Latte.")
        moneyEnterance()
    elif productNumber == 2 and balance >= 2 and americano > 0:
        americano = americano - 1
        balance = balance - 2
        print("Here is your americano.")
        moneyEnterance()
    elif productNumber == 3 and balance >= 1.75 and cappucino > 0:
        cappucino = cappucino - 1
        balance = balance - 1.75
        print("Here is your coffee cappucino")
        moneyEnterance()
    elif productNumber == 4 and balance >= 3 and coolLime > 0:
        coolLime = coolLime - 1
        balance = balance - 3
        print("Here is your cool lime.")
        moneyEnterance()
    elif productNumber == 5 and balance >= 4 and macchiato > 0:
        macchiato = macchiato - 1
        balance = balance - 4
        print("Here is your coffee macchiato.")
        moneyEnterance()
    elif productNumber == 6 and balance >= 1.25 and mocha > 0:
        mocha = mocha - 1
        balance = balance - 1.25
        print("Here is your coffee mocha.")
        moneyEnterance()
    elif productNumber == 7 and balance >= 1.00 and tea > 0:
        tea = tea - 1
        balance = balance - 1.00
        print("Here is your coffee tea.")
        moneyEnterance()
    elif productNumber == 8 and balance >= 0.50 and water > 0:
        water = water - 1
        balance = balance - 0.5
        print("Here is your water.")
        moneyEnterance()
    elif productNumber == 9 and balance >= 2 and hotChocolate > 0:
        hotChocolate = hotChocolate - 1
        balance = balance - 2
        print("Here is your hot chocolate.")
        moneyEnterance()
    elif productNumber == 10 and balance >= 2.25 and whiteHotChocolate > 0:
        whiteHotChocolate = whiteHotChocolate - 1
        balance = balance - 2.25
        print("Here is your White Hot Chocolate.")
        moneyEnterance()
    elif coffeeLatte == 0 or americano == 0 or cappucino == 0 or coolLime == 0 or macchiato == 0 or mocha == 0 or tea == 0 or water == 0 or hotChocolate == 0 or whiteHotChocolate == 0:
        print("No quantity of this product. Please order different thing.")
        productService()
    else:
        print("Not enough money.")
        moneyEnterance()

def moneyEnterance():
    global balance
    global menu
    print("For seeing your current balance and continue shopping press a,to end the process please press b:".format(balance))
    answer = str(input())
    answer = answer.lower()
    if answer == 'a':
        print("Your balance is {}.".format(balance))
        print("To add money press a, to continue to shopping press b: ")
        shopping = str(input())
        shopping = shopping.lower()
        if shopping == 'a':
            coin = eval(input("Enter amount of your money:"))
            balance = balance + coin
            moneyEnterance()
        elif shopping == 'b':
            print(menu)
            productService()
        else:
            print("Invalid input.")
            moneyEnterance()
    elif answer == 'b':
            print("Thank you for using the machine. Here is your money ${0:.2f}.".format(balance))
    else:
        print("Invalid input.")
        moneyEnterance()


def main():
    moneyEnterance()

main()




    

