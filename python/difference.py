list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7]
index1 = 0
newlist = []
while index1<len(list1):
	if (list1[index1] not in list2): 
		newlist.append(list1[index1])
	index1 = index1+1
print newlist


