n = int(input("Enter the original number of coins: "))
coins = list(map(int, input("Enter the coin numbers: ").split()))

count = {}

for i in coins:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for i in count:
    if count[i] % 2 != 0:
        print("Missing coin number:", i)
        break