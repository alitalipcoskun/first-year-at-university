website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1
a = " Hello World "
print(a.strip())
#2
a = website.split('.')
website3 = website.lstrip()
website3 = website.rstrip("/:htp")
print(a[1])
print(website3)
#3
print(course.lower())
#4
print(website.count('a'))
#5
print(website.startswith("www"))
print(website.endswith("com"))
#6
print(website.find(".com"))
#7
print(course.isalpha())
a = "contents"
#8
print("{0:50}".format(a.center(50, '*')))
#ljust, rjust
#9
course2 = course.replace(" ", "-")
print(course2)
#10
m = "Hello World"
m = m.replace("World", "There")
print(m)
#11
course4 = course.split(" ")
print(course4)
