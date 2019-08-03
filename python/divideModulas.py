a = 4213
new = []
i = 0
while True:
	j = a%10
	a = a/10	
	if j==0:
		break
	new.append(j)
	i = i+1
print new
index = 2
b = 0
while index<new[b]:
	if new[b]%index==0 or new[b]==1:
		print "Number is not prime"," ",index
		break
	#index = index+1
		#b = b+1	
	#index = index+1	
	else:
		print "Number is prime"
		index = index+1
		b = b+1

