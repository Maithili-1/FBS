for i in range(1,6):
    k=i
    for j in range(1,6-i):
        print(" ", end=' ')
    for j in range(i,i*2):
        print(j, end=' ') 
    for j in range(2*i-2, i-1, -1):
        print(j, end=' ')
    print()