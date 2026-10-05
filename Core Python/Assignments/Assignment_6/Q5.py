for i in range(1,6):
    print(" "* (9-(i+i-1)), end=" ")
    for j in range(1,i+i):
        print("*", end=" ")
    print()