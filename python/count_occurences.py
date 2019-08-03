char_list = ["a","b","a","c","b","c","a","c"]
index = 0
count_list = []
while index<len(char_list):
    char = char_list[index]
    count = 0
    j = 0
    while j<len(char_list):
        if char == char_list[j]:
            count = count+1
        j = j+1
    if [char_list[index],count] not in count_list:
        count_list.append([char_list[index],count])
    index = index+1
print count_list
