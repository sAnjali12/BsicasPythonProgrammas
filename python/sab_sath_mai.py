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
		average1 = elements[index]/count1		
		print "SUM OF EVEN NUMBER",sum1
		print "count1 OF THE EVEN NUMBER",count1
		print "AVERAGE OF THE EVEN NUMBER",average1
		
	else:
		count2 = count2+1		
		sum2 = sum2+elements[index]
		average2 = elements[index]/count2
		print "SUM OF THE ODD NUMBER",sum2
		print "COUNT2 OF THE ODD NUMBER",count2
		print "AVERAGE OF THE ODD NUMBER",average2
	index = index+1

