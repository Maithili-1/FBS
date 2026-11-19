# Solution 1 :-
def removeDup1(li):
    li2 = []
    for ele in li:
        if ele not in li2:
            li2.append(ele)
    return li2

#Solution 2 :-
def removeDup2(li):
    for i in range(len(li)):
        j = i+1
        while j<len(li):
            if li[i]==li[j]:
                li.pop(j)
            else:
                j+=1
    return li

li = [12,45,10,1,89,23,45,100,64,100]
print(f"{li} after removing duplicates using sol 1  :-  {removeDup1(li)}")
print(f"{li} after removing duplicates using sol 2  :-  {removeDup2(li)}")