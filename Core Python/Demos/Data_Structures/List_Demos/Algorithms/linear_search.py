def linear_search(li, search_ele):
    for ind in range(len(li)):
        if(search_ele==li[ind]):
            return ind
    else:
        return -1

li = [12,90,56,34,88,43,100]
ele = int(input("Enter the element to search : "))
res = linear_search(li, ele)

if res!=-1:
    print(f"{ele} is present at index {res}.")
else:
    print(f"{ele} is not present in list.")