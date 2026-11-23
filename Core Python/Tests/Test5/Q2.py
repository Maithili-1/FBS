n = int(input())
coins = list(map(int, input().split()))

for i in coins:
    if coins.count(i) % 2 != 0:
        print(i)
        break
    