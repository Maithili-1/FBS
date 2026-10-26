li = [1, 3, 4, 1, 2, 3, 6, 7, 1, 2, 4]
dict = {}

for ele in li:
    if ele in dict:
        dict[ele] = dict[ele] + 1
    else:
        dict[ele] = 1
        
print(dict)