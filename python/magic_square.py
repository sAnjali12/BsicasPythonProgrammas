magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
# FOR ROW
index1 = 0
while index1<len(magic_square):
	j1 = 0
	sum1 = 0
	while j1<len(magic_square[index1]):
		sum1 = sum1+(magic_square[index1][j1])
		j1 = j1+1	
	index1 = index1+1
print sum1
#DAIGONAL
index2 = 0
j2 = 0
sum2 = 0
while index2<len(magic_square):
	sum2 = sum2+(magic_square[index2][j2])
	j2=j2+1
	index2 = index2+1
print sum2
i=0
j=-1
sum=0
while i<len(magic_square):
	sum=sum+(magic_square[i][j])
	j=j-1
	i=i+1
print sum
#COLLON
i=0
while i<len(magic_square):
	j=0
	sum=0
	while j<len(magic_square[i]):
		sum=sum+magic_square[j][i]
		j=j+1
	i=i+1
print sum
total_sum = sum1+sum2+sum+sum
print total_sum










