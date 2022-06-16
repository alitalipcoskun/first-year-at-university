"""""
    Yorum satırı ile yazdığınız kısım help(functionName) ile return edilir.
"""
# n = m[:] kopyalama işlemidir adres gösterme degil
# n = m m bir liste ve n ise adres gösterir.

def add(*params):
        return sum(params)
#istedigimiz kadar parametreyi bir fonksiyona yönlendirmemizi '*' sağlar.
#params ise tuple olarak yazdırılır.
# '**' ile dict oldugunu belirtiyoruz.

def add_two(*params):
        sum = 0
        for i in params:
                sum += i
        
        return sum
