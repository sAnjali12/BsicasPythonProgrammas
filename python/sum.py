elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
index = 0
sum1 = 0
sum2 = 0
count1 = 0
count2 = 0
while index<len(elements):
	if elements[index]%2==0:
		count1 = count1+1		
		sum1 = sum1+elements[index]
		
	else:
		count2 = count2+1		
		sum2 = sum2+elements[index]
	index = index+1
even_average = sum1/count1
odd_averae  = sum2/count2
print "EVEN AVERAGE:)___",even_average
print "ODD AVERAGE:)_______",odd_aerage
