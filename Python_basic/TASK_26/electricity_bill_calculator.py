print("****ELECTRICITY BILL CALCULATOR****")
unit=float(input("Enter the value of used electricity in kWh:"))
if (unit>0):
    if(unit<=90):
        amount=unit*7
    elif(unit<=150):
        amount=unit*10
    elif(unit<=300):
        amount=unit*15
    else:
        amount=unit*15*1.03
        print("***Additional 3% Charge Applied***")
    print("************************")
    print(f"Total bill= Rs.{amount}")
    print("************************")
else:
    print("Invalid value. Please try again.")