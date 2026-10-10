li = [10, 20, 30, 40, 50, 45, 100, 90]

max = li[0]
smax = 0

for ind in range(1,len(li)):
    if li[ind] > max:
        smax = max
        max = li[ind]
    elif li[ind] > smax:
        smax = li[ind]

print(f"Max : {max}\nSencond max : {smax}.")