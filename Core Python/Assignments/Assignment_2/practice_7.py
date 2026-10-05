num = int(input("Enter the 3-digit number : "))

d1 = num % 10
num = num//10

d2 = num % 10
num = num//10

d3 = num % 10
num = num //10

print("D1 : ",d1)
print("D2 : ",d2)
print("D3 : ",d3)
print("num : ",num)

