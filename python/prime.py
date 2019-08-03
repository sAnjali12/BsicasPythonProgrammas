
user=input("enter no")
i = 2
while i<user:	
	if user%i==0:
		print "not prime ",user
		break	
	i = i+1	
else:
	print "prime"

