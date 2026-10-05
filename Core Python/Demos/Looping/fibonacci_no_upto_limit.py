limit = int(input("Enter the limit : "))

a = -1
b = 1
while True:
    c = a+b
    if c>limit:
        break
    print(c)
    a = b
    b = c