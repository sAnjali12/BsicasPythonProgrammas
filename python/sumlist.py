marks = [
	    [78, 76, 94, 86, 88],
	    [91, 71, 98, 65, 76],
	    [95, 45, 78, 52, 49]]
index = 0
total_marks=0
while index<len(marks):
	j = 0
	sum=0
	while j<len(marks[index]):        
		sum = sum+marks[index][j]
		j = j+1  
	print sum
	total_marks=total_marks+sum
	index = index+1
print total_marks
