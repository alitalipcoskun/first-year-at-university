def getting_student_data():
    student_data = []
    student_name = str(input("Enter Student's Name: "))
    student_data.append(student_name)
    student_surname = str(input("Enter Student's Surname: "))
    student_data.append(student_surname)
    howManyGrade = eval(input("Enter how many grade you will enter: "))
    for i in range(0,howManyGrade):
        grade = int(input(f"Enter Grade{i+1}: "))
        grade = str(grade)
        student_data.append(grade)
    student_data.append("\n")
    return student_data

def storing_student_data():
    student_data = getting_student_data()
    with open("student_datas.txt", "a", encoding="utf-8") as infile:
        for i in range(len(student_data)):
            if i == 0:
                infile.write(student_data[i]+" ")
            elif i == 1:
                infile.write(student_data[i]+":")
            elif i < len(student_data)-2:
                infile.write(student_data[i]+",")
            else:
                infile.write(student_data[i])
        a = infile.tell()
        infile.seek(a+1)
def print_the_student_data():
    with open("student_datas.txt", "r", encoding="utf-8") as infile:
        for line in infile:
            print(line,end="")        
def calculate_average(line):
    list_of_data = line.split(":")
    nameOfStudent = list_of_data[0]
    data_grades = list_of_data[1].rstrip()
    data_grades = data_grades.split(",")
    #print(data_grades) debugger
    sum = 0
    for i in data_grades:
        i = float(i)
        sum += i
    average = (sum/len(data_grades))
    if average >= 90 and average <= 100:
        grade = "AA"
    elif average >= 85:
        grade = "BA"
    elif average >= 80:
        grade = "BB"
    elif average >= 75:
        grade = "CB"
    elif average >= 70:
        grade = "CC"
    elif average >= 65:
        grade = "DC"
    elif average >= 60:
        grade = "DD"
    else:
        grade = "FF"
    return str(nameOfStudent),str(grade)
def giving_average():
    with open("student_datas.txt", "r", encoding="utf-8") as infile:
        for line in infile:
            nameOfStudent, grade = calculate_average(line)
            print(f"{nameOfStudent} Grade: {grade}")
def saving_letter_grades():
    with open("student_datas.txt", "r", encoding="utf-8") as infile:
        with open("letter_grades.txt", "w", encoding="utf-8") as outfile:
            for line in infile:
                name, grade = calculate_average(line)
                outfile.write(name)
                outfile.write(":")
                outfile.write(grade)
                outfile.write("\n")
def main():
    while True:
        print("Select what do you want to do.".center(190, "*"))
        decider = eval(input("1-Entering Student Data\n2-Calculating Grade\n3-Seeing Student Data\n4-Saving Letter Grades\n5-Exit\n"))
        if decider == 1:
            storing_student_data()
        elif decider == 2:
            giving_average()
        elif decider == 3:
            print_the_student_data()
        elif decider == 4:
            saving_letter_grades()
        else:
            break

main()

