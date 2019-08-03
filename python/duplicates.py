n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
index = 0
new_list = []
while index<len(n):
    inteser = n[index]
    j = index+1
    while j<len(n):
        if inteser == n[j]:
            if n[j] not in new_list:
                new_list.append(n[j])
        j =j+1
    index = index+1
print new_list
