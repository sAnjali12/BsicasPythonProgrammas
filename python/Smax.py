numbers = [50,40,23,70,56,12,5,10,7]
index = 0
max_x = 0
while index<len(numbers):
	if max_x<numbers[index]:
		max_x = numbers[index]
	index = index+1
print "max no"+" "+str(max_x)
j = 0
smax= 0
while j<len(numbers):
	if max_x>numbers[j] and smax<numbers[j]:
		smax = numbers[j]
	j = j+1
print "second max_x"+"  "+str(smax)
