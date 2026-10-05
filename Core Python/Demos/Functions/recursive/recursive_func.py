def func(n):
    print("Function executing.")
    if n>1:
        func(n-1)

n = 5
func(n)