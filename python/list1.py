numbers = [50,40,20,30,7,5,12,23,56]
index = 0
while index<len(numbers):
	index = index+1
print index





numbers = [50,40,23,70,12,7,10,56]
i=0
count_no = 0
count1=0
while i<len(numbers):
	if numbers[i]>20 and numbers[i]<40:
		count1=numbers[i]+count1
		count_no=count_no+1
	i=i+1
print "count no:)"+" "+str(count_no)
print "count1:)"+" "+str(count1)


numbers = [50,40,23,70,56,12,5,10,7]
index = 0
max_x = 0
while index<len(numbers):
	if max_x<numbers[index]:
		max_x = numbers[index]
	index = index+1
print max_x




