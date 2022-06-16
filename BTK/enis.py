from calendar import c
from os import ctermid


cities = ["Bursa", "Ankara", "İstanbul", "İzmir", "Kahramanmaraş"]
n = 1
same_length = []
temp = ""
for i in range(len(cities)-1):
    for j in range(len(cities)-1):
        if len(cities[j]) > len(cities[j+1]):
            temp = cities[j]
            #cities[j] = cities[j+1]
            cities.remove(cities[j])
            #cities[j+1] = temp
            cities.insert(j+1, temp)
