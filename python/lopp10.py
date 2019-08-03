i = 5
j = 0
while j<=i:
	user = input("enter your guess")
	if user==i:
		i = i+1
		print "SAHI HAI"
		break
	elif user!=i:	
		print "YAR SACH MAI PAGL HO"
