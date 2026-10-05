for i in range(1,6):
    n = 65
    for j in range(1,6-i):
        print(" ", end=' ')
    for j in range(1,i*2):
        print(chr(n), end=' ')
        n+=1
    print()