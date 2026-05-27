marks=int(input("Enter your marks:"))

if (marks>=75 and marks<=100):
    print("Grade: A")
elif (marks>=65 and marks<=74):
    print("Grade: B")
elif (marks>=50 and marks<=64):
    print("Grade: C")
elif (marks>=35 and marks<=49):
    print("Grade: S")
elif (marks>=0 and marks<=34):    
    print("Grade: W")
else:
    print("Invalid value!")
   