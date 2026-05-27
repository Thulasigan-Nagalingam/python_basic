value=input("Enter a number:")
if (int(value)>0):
    if (int(value)%2==0):
        print(value,"is even number")
    else:
        print(value,"is odd number")
else:
    print("Invalid input! Please enter a positive number")