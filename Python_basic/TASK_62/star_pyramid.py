z=int(input("Enter the number of rows:"))
for x in range(1,(z+1)):
    for y in range(1,(z+1)):
        print("*",end=" ")
        if(x==y):
            break
    print("")
    