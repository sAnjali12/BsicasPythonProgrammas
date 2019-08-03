elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
even_list = []
odd_list = []
while index<len(elements):
	if elements[index]%2== 0:
		even_list.append(elements[index])
	else:
		odd_list.append(elements[index])
	index = index+1
print even_list,"Is a Even"
print odd_list,"Is a odd"
Even = 0
E_sum = 0 
while Even<len(even_list):
	E_sum = E_sum+(even_list[Even])
	Even = Even+1
Odd = 0
O_sum = 0
while Odd<len(odd_list):
	O_sum = O_sum+(odd_list[Odd])
	Odd = Odd+1
print "EVEN SUM :)_______",E_sum
print "ODD SUM :)_________",O_sum

