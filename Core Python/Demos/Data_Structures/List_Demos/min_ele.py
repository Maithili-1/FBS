def minEle(li):
    min = li[0]
    for i in range(1,len(li)):
        if li[i] < min:
            min = li[i]
    return min

li = [12,45,10,1,89,23,64]
print(f"Min element in {li} is {minEle(li)}.")