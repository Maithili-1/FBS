'''1   2  3  4  5 
   6   7  8  9 10 
   11 12 13 14 15 
   16 17 18 19 20 
   21 22 23 24 25 '''

k = 1
for i in range(1,6):
    for j in range(1,6):
        print(k, end=" ")
        k+=1
    print()


print()

''' * * * * * * 
    * 3 4 5 6 * 
    * 4 5 6 7 * 
    * 5 6 7 8 * 
    * 6 7 8 9 * 
    * * * * * * '''
for i in range(1,7):
    for j in range(1,7):
        if(i==1 or i==6 or j==1 or j==6):
            print("*", end=" ")
        else:
            print(i+j-1, end=" ")
    print()
   
    
print()


'''    * 
      * * 
     * * * 
    * * * * 
     * * * 
      * * 
       *    '''

### Solution 1

for i in range(1,5):
    print(" "*(4-i), end = " ")
    for j in range(1,i+1):
        print("*", end=" ")
    print()

for i in range(1,4):
    print(" "*i, end=" ")
    for j in range(1,(5-i)):
        print("*", end=" ")
    print()


print()   
  
  
### Solution 2
   
for i in range(1,5):
    print(" "*(4-i) + "* "*i)

for i in range(3,0,-1):
    print(" "*(4-i) + "* "*i)
    
    
k=100    
for i in range(1,11):
    if(i%2!=0):
        for j in range(1,11):
            print(k, end=" ")
            k-=1
    else:
        n = k
        for j in range(1, 11):
            print(n-10+j, end=" ")
            #n+=1
        k-=10
    print()