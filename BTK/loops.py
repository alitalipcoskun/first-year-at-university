urunler = [ {'name': 'samsung s6', 'price': '3000'}, {'name': 'samsung s7', 'price': '4000'}, {'name': 'samsung s8', 'price': '5000'}, {'name': 'samsung s9', 'price': '6000'}, {'name': 'samsung s10', 'price': '7000'}]

total_cost = 0
for i in urunler:
	total_cost += eval(i['price'])
	if eval(i['price']) <= 5000:
		print(i['name'])

print(total_cost)
#enumerate(list_name) returns two things, index and list value, as tuple.
#zip method returns a tuple, listeleri eşleştiren tuplelar return eder.

numbers = [x for x in range(10)]
