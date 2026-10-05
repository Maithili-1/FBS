n = int(input("Enter value of n : "))

sum = 0
for i in range(1,n+1):
    sum += n**i
print(f"Sum of series = {sum}.")