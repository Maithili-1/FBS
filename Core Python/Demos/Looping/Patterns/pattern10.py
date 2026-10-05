for i in range(1,6):
    for j in range(1,6):
        if(j==1 or i==5 or j==i):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()