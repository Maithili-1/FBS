li = [10, 20, 30, 40, 50, 45, 100, 90]

max = li[0]
for ind in range(1, len(li)):
    if (li[ind] > max):
        max = li[ind]

print(f"Max element in {li} is {max}.")