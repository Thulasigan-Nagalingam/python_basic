print("***********Welcome to ASMD Calculator***********")
print("****Choose a operational funtions as number****")
print("***********************************************")
print("Addition(+)=1")
print("Subtraction(-)=2")
print("Multiplication(x)=3")
print("Division(/)=4")
print("***********************************************")


num1= int (input("Enter the first number:"))
num2= int (input("Enter the second number:"))
function=int(input("Enter the operational funtion's number:"))

match function:
    case 1:
        print("Answer =",num1+num2)
        
    case 2:
        print("Answer =",num1-num2)
        
    case 3:
        print("Answer =",num1*num2)
        
    case 4:
        print("Answer =",num1/num2)
        
    case _:
        print("Invalid operational function! Please try again")