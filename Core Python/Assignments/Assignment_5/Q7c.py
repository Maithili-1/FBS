#Format :- a + ar + ar^2 + ar^3...   r=common ratio

n = int(input("Enter value of n : "))

# 1st way
sum = 0
a = 1
for i in range(n):
    sum += a
    a *= 2
print(f"Sum of series = {sum}.")

# 2nd way
sum = 0
a = 1
for i in range(n):
    sum += a*(2**i)
print(f"Sum of series = {sum}.")