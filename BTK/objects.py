string_usage = "I am ali."
print(string_usage[start:end:kacarkacararttıgı])
name = "Ali Talip"
surname = "Coskun"
age = 22
print("My name is {0}, and my surname is{1}".format(name, surname))
print("My name is {n}, and my surname is{s}".format(n=name, s=surname))
print("My name is {0}, and my surname is{1}\nMy age is {}".format(name, surname,age))

result = 2/9
print("The result is {r:1.4}".format(r=result)) ## sol kısım tam karakter için kaç boşluk bırakacağını ayarlar, sağ kısım ise noktadan sonra kaç rakam yazılacağını yönetmemizi sağlar.
## f string olarak yazım
print(f"My name is {name} {surname}. I am {age} years old")


