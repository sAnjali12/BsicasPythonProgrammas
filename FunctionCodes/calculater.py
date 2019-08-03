def calculator(number_x,number_y,operation):
	if operation == "add":
		add_numbers = number_x + number_y
		sum = add_numbers
	elif operation == "subtract":
		sub_numbers = number_x - number_y
		sum = sub_numbers
	elif operation == "multiple":
		multi_numbers = number_x * number_y
		sum = multi_numbers
	else:
		divide_numbers = number_x / number_y
		sum = divide_numbers
	print "Add,Sub,Multi,Divide in both numbers"
	return sum

num = calculator(123,567,"add")
print num
num1 = calculator(567,123,"subtract")
print num1
num2 = calculator(89,90,"multiple")
print num2
num3 = calculator(1944556663332288,2345678,"divide")
num3
