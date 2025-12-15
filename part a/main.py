from registration_system import System

members = {
    "Jason","18" , "Student",
    "Jannah", "28","Adult"
}

#Add a new book from user input
Name= str (input("Please Enter your Name:"))
Age= int (input("Please enter your age:"))
Membership = str (input("Please enter your membership type:"))
members = [Name,Age,Membership]

#Save to file
with open("Swimming Pool Registration System.txt" , "w") as f:
    for n,a,m in members():
        f.write (f"{n}:{a}:{m}\n")

#Read back from file
with open ("Swimming Pool Registration System.txt" , "r") as file:
    lines = file.readlines()

print("\n Book List from File:")
for line in lines:
    n,a,m = line.strip().split(",")
    m= members (n,a,m)
    m.display_info()