user_id=input("Enter the User ID:")
password=input("Enter the password:")
role=input("Enter your role(admin1/user)")

if((user_id=="Yarl_IT") and (password=="123585321")):
    print("login Successful")
    print("Welcome to Yarl IT")
    if (role="admin1"):
        print("Welcome to admin panel")
    elif (role="user"):
        print("Welcome to user dashboard")
    else:
        print("Sorry! Incorrect role. Please try again")
else:
    print("Sorry! Invalid user_id,password ")
    