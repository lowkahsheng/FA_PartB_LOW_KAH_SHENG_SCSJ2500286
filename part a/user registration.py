import datetime

print ("Welcome to the public swimming pool!")

Name= str (input("Please Enter your Name:"))
Age= int (input("Please enter your age:"))
Membership = str (input("Please enter your membership type:"))

print("Name:", Name, "Age:", Age, "Membership Type:", Membership)

if Age < 12 :
    print("Not eligible for membership")
elif Age >= 12 :
    print("Standard membership granted")
elif Age >60 :
    print("Senior membership granted")
