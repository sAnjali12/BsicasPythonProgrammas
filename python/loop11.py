i = 5
j = 0
while j<=5:
	user = input("enter your guess")
	if user==i:
		i = i+1
		print "SAHI HAI"
		break
	if user<i:	
		print "AAPKA NUMBER CHHOTA HAI"
	if user>i:
		print "AAPKA NUMBER BDA HAI"
	else:
		print "YAR OR KITNA PAGL SMJHU"
		break
