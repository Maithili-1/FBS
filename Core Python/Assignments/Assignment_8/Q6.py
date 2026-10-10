def fibonacci(n):
    a = -1
    b = 1
    for i in range(n):
        c = a+b
        print(c)
        a = b
        b = c
        
n = int(input("Enter the value of n : "))
fibonacci(n)