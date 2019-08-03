def maximum(list,n):
	if(n==1):
	    return list[0]
	if list[n-1]>maximum(list,n-1):
	    return list[n-1]
	else:
	    maximum(list,n-1)
maximum ([23,45,12,67,89,34],4)
