def is_harshad_number():
	harshad_number = 42
	string = list(str(harshad_number))
	index = 0
	sum = 0
	while index<len(string):
		sum = int(string[index])+sum
		index = index+1
		if harshad_number%sum==0:
			print "this is harshad number",harshad_number
	return sum
	
sum_of_digite = is_harshad_number()
print sum_of_digite
