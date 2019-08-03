start_num = int(input("enter your start number"))
end_num = int(input("enter your end number"))
while (start_num<=end_num):
	count = 0
	i = 2
	while (i<=start_num/2):
		if (start_num):
			print "number is not prime"			
			count = count+1
			break
		i = i+1
	if (count==0 and start_num!=1):
		print "prime number"
	start_num = start_num+1

