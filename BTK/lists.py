#result = 'Mercedes' in arabalar # arabalar listesinde mercedes varsa true yoksa false degerini return eder.
#arabalar[-2:] = [x,y] son iki değeri x ve y ile degistirir.
#arabalar + ['Audi', 'Nissan'] son iki eleman olarak ekleme yapar.
# del arabalar[-1] indexteki elemanı siler.

#liste methodları

numbers = [2,5,123,4,213,32,12,412,2]
letters = ['a', 'g', 'b', 's', 'y', 'a', 'm']
val = min(numbers)
val2 = max(numbers)
numbers.append(31)
numbers.insert(#index, #eleman)
numbers.pop() #son elemanı siler
numbers.pop(#index girersen o indexteki elemanı siler)
numbers.remove(2) #elemanı arar ve siler
numbers.sort() #sayısal veya alfabetik olarak sıralar
len(numbers) # kaç eleman oldugunu söyler
letters.count('a') #elemanın kaç tane oldugunu söyler.

