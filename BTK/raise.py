#x = 10
#if x > 5:
#    raise Exception("x 5'ten büyük olamaz")
#
#def check_password(psw):
#    import re
#    if len(psw) < 8:
#        raise Exception("Parola en az 7 karakter olmalıdır.")
#    elif not re.search("[a-z]", psw):
#        raise Exception("parola küçük harf içermelidir.")
#    elif not re.search("[A-Z]", psw):
#        raise Exception("parola büyük harf içermelidir.")
#    elif not re.search("[0-9]", psw):
#        raise Exception("parola rakam içermelidir.")
#    elif not re.search("[_@$]", psw):
#        raise Exception("parola özel karakter içermelidir.")
#    elif re.search("\s", psw):
#        raise Exception("parola boşluk içermemelidir.")
#
#password = "12345678aA_"
#
#try:
#    check_password(password)
#except Exception as ex:
#    print(ex)
#else:
#    print("parolanız oluşturuldu.")
#finally:
#    print("işlem tamamlandı.")

class Person:
    def __init__(self, name, year):
        self.year = year
        if len(name) > 10:
            raise Exception("Name alanı fazla karakter taşıyor.")
        else:
            self.name = name
        if year < 1000 or year > 2022:
            raise Exception("Geçerli bir yıl giriniz")
        else:
            self.year = year

p = Person("Ali", 1999)
m = Person("Jesus", -700)


