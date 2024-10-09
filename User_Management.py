#The basic structure is of a class inside which we have a dictionary containing all the information of the user, with email as key and a dictionary as value.


class User():
    def __init__(self, emailid, password, first_name, last_name, age): #Created a dictionary of various info and giving it as a value to dictionary id whose key will be the emailid
        info = {}
        info["password"]= password
        info["first_name"] = first_name
        info["last_name"]  = last_name
        info["age"] = age
        self.user_data = info
    
    def verify_credentials(self, email, password, first_name, last_name, age):
        if email not in self.keys():
            print("email ID not found! Please try again.")
        if self.user_data[email]["password"] != password :
            print("Incorrect password. Please try again.")
        
        print("Logged in successfully")
'''Defining all the required functions to support the program'''
def input_choice():
    '''
    Documentation for the input_choice()
    Takes an input and makes sure exceptions are handled
    '''
    while(1):
        try:
            choice = int(input("Choose an option (1,2 or 3): "))
        except:
            print("Invalid input!")
        else:
            return choice
            
def input_email():
    '''
    Documentation for input_email()
     
    This function takes specifically an email as an input, checks if it is a valid email
    or not  and returns the email as a string.
    '''
    while(1):
        try:
            emailid = input("Enter your email ID: ")
            if '@' not in emailid:
                raise Exception
        except:
            print("Invalid Email ID entered! Please try entering your email ID again.")
        else:
            return emailid
    
def input_age():
    '''
    Documentation for the input_age()
    This function will take age as an input and check all the exceptions possible and return the age.
    '''
    while(1):
        try:
            age = int(input("Enter your age : "))
            if age == 0:
                print("Age cannot be zero! Please try again")
                continue
            elif age <0 :
                print("Age cannot be negative! Please try again")
                continue
        except:
            print("Age should be an integer. Please try again.")
        else:
            return age


'''All required functions defined'''
choice = 0
user = User("unknown@sample.com","123@13","Melon","Jay", 20)
while(choice != 3 and choice != 1):#Will exit when user enters choice as 3
    print("Menu :")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")
    
    choice = int(input("Choose an option (1,2 or 3): "))
    
    if choice == 1:
        emailid = input_email()
        #If email already exists, we need to raise an error
        if  emailid in user.user_data.keys():
            print("Email ID already exists. Please try again.")
            continue
            
        password = input("Enter your password: ")
        
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        
        age = input_age()
        
        user.user_data[emailid] = {emailid,password,first_name,last_name,age}
    
print(user.user_data)
        
        
        
        
