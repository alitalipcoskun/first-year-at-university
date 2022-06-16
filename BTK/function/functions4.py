def processing(process_name):
    def summing(*args):
        sumOfthem = 0
        for i in args:
            sumOfthem += i
        return sumOfthem
    def multiplication(*args):
        multiplying = 1
        for i in args:
            multiplying *= i
        return multiplying
    if process_name.capitalize() == "Summing":
        return summing
    elif process_name.capitalize() == "Multiplication":
        return multiplication
    else:
        return "ERROR"

a = processing("Summing")
b = processing("multiplication")
listOfInts = (1,3,4,1242,123,32)

print(a(3,5,7,6))
print(b(23,13,13))