from datetime import date, datetime


result = datetime.now() # == datetime.today()
#result = result.year
#result = result.month
#result = result.day
#result = result.hour
#result = result.minute
#result = result.second
#result = datetime.ctime(result)
result = datetime.strftime(result, '%Y') #%X saat bilgisini verir.(saniye dahil), %D day bilgisi, %A gün bilgisini verir, %B ay bilgisini verir.
#istedigin kadar parametre girebilirsin. %Y, %X gibi.
print(result)
t = "25 January 2021 hour 16:21:31"
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
print(dt)
birthday = datetime(1999, 11,24,10,23,00)
result = datetime.timestamp(birthday) #saniye
result = datetime.fromtimestamp(result)
a = datetime.fromtimestamp(0)
result = result - a
print(result)
print(a)