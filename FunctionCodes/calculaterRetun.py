def calculator(operation,number_x,number_y):
	number_x = int(raw_input("enter your nuber"))
	number_y = int(raw_input("enter your second number"))
	if operation == "add":
		add_numbers = number_x + number_y
		add_result = add_numbers
		print "addition of two numbes"
		return add_result
	elif operation == "subtract":
		sub_numbers = number_x - number_y
		subtract_result = sub_numbers
		print "sunbstraction of two numbers"
		return subtract_result
	elif operation == "multiple":
		multi_numbers = number_x * number_y
		multiply_result= multi_numbers
		print "multiplication of two numbers"
		return multiply_result
	else:
		divide_numbers = number_x / number_y
		divide_result = divide_numbers
	print "Division of two numbers"
	return divide_result
num1 = calculator("add","number_x","number_y")
print num1
num2 = calculator("subtract","number_x","number_y")
print num2
num3 = calculator("multiple","number_x","number_y")
print num3
num4 = calculator("divide_result","number_x","number_y")
print num4
print divide_result




