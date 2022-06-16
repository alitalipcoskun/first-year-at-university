message = "ben mal miyim"
message = message.upper() #harfleri büyütür.
message = message.lower() #harfleri küçültür.
message = message.title() # ifadeyi başlık olacak şekilde kelimelerin ilk harfini büyütür.
message = message.capitalize() #ifadenin sadece ilk harfini büyütür.
message = message.strip() #baş ve sondaki karakterleri siler.
#b = message.split("içine ayıracagımız ifadeyi tırnak içinde belirtebiliriz. " " gibi.) stringdeki her kelimeyi liste halinde return eder."""

#"a = ' '.join(b) listedeki kelimeleri birer boşluklu halde yazmamızı sağlar veya nasıl istersen o şekilde."""
index = message.find("mal")#buldugu kelimenin ilk harfinin index numarasını yönlendirir. -1 return ederse bu kelimenin stringte olmadıgı anlamı çıkmalıdır.
isFound = message.startswith('b') #stringin hangi harfle başladıgını bool ifade olarak return eder.
isFound = message.endswith('m')
message = message.replace("mal", "zeki")
print(message)
