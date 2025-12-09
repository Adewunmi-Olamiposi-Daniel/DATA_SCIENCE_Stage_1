# DSWK2D6 MINI PROJECT
# LOGIN SYSTEM WITH ERROR HANDLING

# Dataset of users
users = {
    "klaus": {
        "password": "DataKing123",
        "role": "admin",
        "email": "klaus@gmail.com",
        "security_q": "What is the name of your first PC?",
        "security_a": "hp"
    },
    "sarah": {
        "password": "pass1254",
        "role": "CFO",
        "email": "sarah2002@gmail.com",
        "security_q": "What is your favourite color?",
        "security_a": "blue"
    },
    "alex": {
        "password": "pythonIsKey111",
        "role": "Coder",
        "email": "alexxx@yahoo.com",
        "security_q": "What city do you live in?",
        "security_a": "lagos"
    }
}

# Activity Logs
activity_log=[]

#Login Function
def login():
    attempts=0
    while attempts < 3:
        try:
            username=input("Enter Username: ").strip().lower()
            password=input("Enter Password: ").strip()
            
            #Handle username not found
            if username not in users:
                raise KeyError("Username does not exist")
            
            #Handle incorrect password
            if users[username]["password"] != password:
                attempts+=1
                activity_log.append(f"Failed login for user '{username}'. Wrong password")
                print("Incorrect password,try again")
                continue

            #If login successful
            activity_log.append(f"Successful login for user '{username}'")
            print(f"Login successful. Welcome {username}")
            print(f"Your role is:{users[username]['role']}")
            return username
        
        except KeyError:
            attempts+=1
            activity_log.append("Login failed. Username not found")
            print("This username does not exist")
        except ValueError:
            attempts+=1
            activity_log.append("Login failed. Invalid input type")
            print("You have entered an invalid input type")
        
    #After 3 failed attempts
    print("\nYou have attempted 3 times.")
    return None
#Password reste function
def password_reset(username):
  print("\nPassword reset requested.")
  #Verify security questions
  question=users[username]["security_q"]
  answer=users[username]["security_a"]
  print("Security question: ",question)
  user_ans=input("Answer here: ").strip().lower()

  if user_ans != answer:
      print("Security answer incorrect.Cannot reset password.")
      activity_log.append(f"Password reset failed for '{username}'. Security answer wrong")
      return
  
  #Allowing a new password
  new_pass=input("Enter your new password: ").strip()
  users[username]["password"]=new_pass

  print("Password reset successful.")
  activity_log.append(f"Password reset successful for '{username}'")

#Main program flow.
username = login()
if username is None:
    choice = input("Would you like to reset your password? (yes/no)").strip().lower()
    if choice=="yes":
        #Ask for username for password reset
        uname=input("Enter your username for reset: ").strip().lower()

        if uname in users:
            password_reset(uname)
        else:
            print("Username not found, cannot reset password.")
else:
    print("\nSystem ready. You are logged in.")

    #Print activity logs
print("\n Activity logs:")
for log in activity_log:
    print(log)