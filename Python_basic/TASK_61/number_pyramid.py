z=int(input("Enter the number of rows within 100: "))
for x in range (1,(z+1)):
    for y in range (1,(z+1)):
        if (y<10):
            print(y,end=" ")
        else:
            print(y,end="")
        if (x==y):
            break
    print('')