#The basic structure is of a class inside which we have a dictionary containing all the information of the user, with email as key and a dictionary as value.


class User():
    def __init__(self, emailid, password, first_name, last_name, age): #Created a dictionary of various info and giving it as a value to dictionary id whose key will be the emailid
        info = {}
        info["password"]= password
        info["first_name"] = first_name
        info["last_name"]  = last_name
        info["age"] = age
        
        self.user_data[emailid] = info
    
    def verify_credentials(self, email, password, first_name, last_name, age):
        if email not in self.keys():
            print("email ID not found! Please try again.")
        if self.user_data[email]["password"] != password :
            print("Incorrect password. Please try again.")
        
        print("Logged in successfully")

'''Defining all the required functions to support the program'''

def input_email():
''' This function takes specifically an email as an input and returns '''



choice = 0

while(choice != 3):#Will exit when user enters choice as 3
    print("Menu :")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")
    
    choice = int(input("Choose an option (1,2 or 3): "))
    if choice == 1:
        emailid = input_email()
        password = input("Enter your password: ")
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = input_age()
        
        
        
        

