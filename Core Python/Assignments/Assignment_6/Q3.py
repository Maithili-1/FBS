""" WAP to print following pattern 
         1
       1   1
      1  2   1 
     1  3  3   1
 """

for i in range(1,5):
    print(" "*(4-i), end=" ")
    for j in range(1,i+1):
        if(j==1 or j==i):
            print(1, end=" ")
        else:
            print(i-1, end=" ")
    print()