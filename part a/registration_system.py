class System:
    def _init_(Name,Age,Type):
        Name = Name
        Age = Age
        Type = Membership

Name= str (input("Please Enter your Name:"))
Age= int (input("Please enter your age:"))
Membership = str (input("Please enter your membership type:"))

def display_info():
    print("Name:", Name, "Age:", Age, "Membership Type:", Membership)