marks = [
	    [78, 76, 94, 86, 88],
	    [91, 71, 98, 65, 76],
	    [95, 45, 78, 52, 49]]
index = 0
total_sum=0
while index<len(marks):
	j = 0
	sum=0
	count = 0	
	while j<len(marks[index]):        
		sum = sum+marks[index][j]
		count = count+1		
		average = sum/count
		
		j = j+1  
	print sum
	print average	
	total_sum=total_sum+sum	
	index = index+1
print total_sum
#print  average
