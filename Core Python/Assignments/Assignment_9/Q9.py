def mPowerN(m,n):
    if n==0:
        return 1
    else:
        return m * mPowerN(m, n-1)

m = int(input("Enter the value of m : "))
n = int(input("Enter the value of n : "))
print(f"{m}^{n} = {mPowerN(m,n)}.")