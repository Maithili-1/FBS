### 1) "pass" == To neglect indented block error
for i in range(1,5):
    pass

### 2) "break" == To terminate the loop
for i in range(1,5):
    if(i==3):
        break
    print(i)
    
    
### 3) "continue" == To stop current iteration
for i in range(1,5):
    if(i==3):
        continue
    print(i)
    

### 4) "else:" == Will be execute when loop executed successfully.
for i in range(1,5):
    if(i==3):
        continue
    print(i)
else:
    print("Else block executed.")
    
    
for i in range(1,5):
    if(i==3):
        break
    print(i)
else:
    print("Else block executed.")