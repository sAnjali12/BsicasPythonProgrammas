elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
sum1 = 0
sum2 = 0
while index<len(elements):
	if elements[index]%2==0:
		sum1 = sum1+elements[index]
		
	else:
		sum2 = sum2+elements[index]
	index = index+1
print sum1,"EVEN SUM __________"
print sum2,"ODD SUM_____"
