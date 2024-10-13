'''
This program uses a functional approach to apply a user data management system
A dictionary is used to store all user's data
'''

'''Defining all the required functions to support the program'''

def input_choice():
    '''
    Documentation for the input_choice()
    Takes an input and makes sure exceptions are handled
    '''
    count =0
    while(count<5): #Will tolerate maximum of 5 incorrect entries
        try:
            choice = int(input("Choose an option (1,2 or 3): "))
        except:
            print("Invalid input!")
        else:
            return choice
        finally:
            count += 1
    if count>=5 :
        print("Too many incorrect inputs, please try after sometime.")
        exit()
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

    print("Logged in successfully")
'''All required functions defined'''
choice = 0
users = {
    "abc@example.com":{"password":"abcd123","first_name":"Doug","last_name":"Moncanda","age":34},
    "xyz@domain.in":{"password":"marian789","first_name":"Mary","last_name":"Joes","age":28}
    
}
while(1):#Will exit when user enters choice as 3 or if user signed in
    print("Menu :")
    print("1. Signup")
    print("2. Sign-in")
    print("3. Exit")
    
    choice = input_choice()
    
    if choice == 1:
        emailid = input_email()
        #If email already exists, we need to raise an error
        if  emailid in users.keys():
            print("Email ID already exists. Please try again.")
            continue
            
        password = input("Enter your password: ")
        
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        
        age = input_age()
        
        info = {"password":password,"first_name":first_name,"last_name":last_name,"age":age}
        
        users[emailid] = info
    
    
    elif choice == 2:
        emailid  =  input_email()
        
        while(1):
            password = input("Enter your password: ")
            if emailid not in users.keys():#If emailid not found in our data, we ask user to choose to sign-up or sign-in again.
                print("No data of this Email ID found. Kindly sign-up or sign in again using a different email.")
                break
            elif users[emailid]["password"] == password : #If the password in our system and input password matches, user is signed in
                print("Signed In Successfully. ")
                exit()
            else :
                print("Invalid password. Please try again")
                
    
    elif choice == 3 :
        print("Exiting the application. Goodbye!")
        break
        
    else :
        print("The choice must be in between 1-3. Please try again")

        
        
