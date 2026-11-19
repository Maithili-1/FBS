li = [3,9,10,14,1,2,6,17]

count = 0
for i in range(len(li)):
    if(li[i] % 2 !=0):
        count+=1
        if count%2!=0:
            print(li[i])

