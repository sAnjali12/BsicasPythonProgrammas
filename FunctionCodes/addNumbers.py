def add_numbers(num1,num2):
	print "I add the two numbers."
	add1 = num1+num2
	print "Two numbers sum of",add1,"\n"
add_numbers(56,12)












def add_numbers_list(list1,list2):
	i = 0
	sum = 0
	while i<len(list1):
		sum = list1[i]+list2[i]
		print "sum of indexes",sum
		i = i+1
add_numbers_list([50, 60, 10],[10, 20, 13])
	
