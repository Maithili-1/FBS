def bubbleSort(li):
    size = len(li)
    for i in range(1,size):
        for j in range(0, size-i):
            if li[j]>li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]


li = [12,90,56,34,88,43,100]
print('Before Sorting : ',li)
bubbleSort(li)
print('After Sorting : ',li)