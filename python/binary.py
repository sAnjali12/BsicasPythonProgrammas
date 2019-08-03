binary_number = [1, 0, 0, 1, 1]
x = 0
sum = 0
index = len(binary_number)-1
while index>=0:
	solve =(binary_number[index])*(2**x)
	sum = sum+solve
	index = index-1
	x=x+1
print sum

