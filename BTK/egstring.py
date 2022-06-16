website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sonra Python Programlama Rehberiniz (40 Saat)"
#1
print(len(course))
#2
print(website[7:10])
#3
print(website[-1:-4:-1])
#4
print(course[0:15:1])
print(course[-1:-16:-1])
#5
print(course[-1: :-1])

name, surname, age, job = "Bora", "Yılmaz", 32, "Engineer"
#6
print("My name is {} {}. I am {} years old. My job is {}.".format(name, surname, age, job))
print(f"My name is {name} {surname}. I am {age} years old. My job is {job}.")
#7
a = "Hello world"
print(a[0:6]+"W"+a[7:])
a.replace('w', 'W')
print(a)
print("abc"*3)

