data =  [[101,"Seema",45000],[340,"Rajani",13000],[210,"Tannu",14000],[320,"Suresh",35000]]

print(f"List before sorting : {data}")

size = len(data)
for i in range(1, size):
    for j in range(size-i):
        if data[j][2] > data[j+1][2]:
            data[j], data[j+1] = data[j+1], data[j]

print(f"List after sorting : {data}")


#Using in-built method :- 
# data.sort(key = lambda x : x[2])
