def list_change(list1,list2,operation):
	index = 0
	new_list = []
	while index<len(list1):
		if operation == "multiply":
			var_x = list1[index]*list2[index]
			new_list.append(var_x)
		index = index+1
	print "Multiplication of list indexsx:)__________",new_list
list_change([5, 10, 50, 20], [2, 20, 3, 5],"multiply")
