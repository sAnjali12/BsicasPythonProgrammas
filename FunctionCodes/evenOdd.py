def check_numbers(list1):
	index = 0
	while index<len(list1):
		if list1[index]%2==0:
			print "It is even numbers",list1[index]
		else:
			print "it is not even numbers",list1[index],"\n"
		index = index+1
check_numbers([23,45,67,89,10,43,52])





def check_numbers_list(list1,list2):
	index = 0
	while index<len(list1):
		if list1[index]%2==0 and list2[index]%2==0:
			print "Both are is even number! ","1.) first number is",list1[index],"\n","2.) second number is",list2[index]
		else:
			print "Both are is not even number! ","1.) first number is",list1[index],"\n","2.) second number is",list2[index]
		index = index+1
check_numbers_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87] )
