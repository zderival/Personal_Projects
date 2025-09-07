import random
from datetime import datetime
import time
from Profile import Profile
# Will soon be an actual database
user_storage = {}
temp_id_storage = {}
class User:
    def __init__(self, id, dob, username, password, email, newUser = True):
        self.id = id
        self.DOB = dob
        self.username = username
        self.password = password
        self.email = email
        self.newUser = newUser
        self.profile = Profile(username,email,password,id,saved_article= [],profile_pic=None,display_color=None,newUser = True)

def generate_id(user_storage):
    while True:
        id = str(random.randint(00000, 99999))
        if id not in user_storage:
            return id
def createaccount():
    class InvalidUserSetup(Exception):
        pass
    username = ""
    while True:
        try:
            username = input("Enter your Username: ")
            if len(username) < 8 or len(username) > 32:
                raise InvalidUserSetup("Username must be 8-32 characters")
            break
        except InvalidUserSetup as e:
            print(e)
    email = input("Enter your email: ")
    dob = ""
    while True:
        try:
            dob_input = input("Date of birth (ie: MM/DD/YYYY): ")
            month, day, year = map(int, dob_input.split("/"))
            dob_date = datetime(year, month, day)
            today = datetime.now()
            age = today.year - dob_date.year - ((today.month, today.day) < (dob_date.month, dob_date.day))
            if age < 15:
                raise InvalidUserSetup("You can not access this app")
            break
        except InvalidUserSetup as e:
            print(e)
            time.sleep(5)
            exit()
        except ValueError:
            print("Invalid date format. Please enter MM/DD/YYYY")

    # A blocker would prevent the user from accessing it
    password = ""
    while True:
        try:
            password = input("Enter your password: ")
            if len(password) < 8 or len(password) > 32:
                raise InvalidUserSetup("Password must be 8-32 characters")
            elif not any(password.upper() for char in password) or not any(password.lower() for char in password):
                raise InvalidUserSetup("Must contain at least must 1 upper case and 1 lowercase letter")
            elif not any(char.isdigit() for char in password):
                raise InvalidUserSetup("Must have at least one digit in your password")
            break
        except InvalidUserSetup as e:
            print(e)
    while True:
        confirm = input("Re enter your password: ")
        if password != confirm:
            print("Passwords don't match")
        else:
            break
    id = generate_id(user_storage.keys())
    user = User(id, dob, username, password, email, newUser=True)
    user_storage[id] = user
    temp_id_storage[id] = user
    print("Account created")
#if new user selects create  account

#else: login: the user inputs username/email and their password:
def login():
    login = False
    user_email = input("Enter your username/email: ")
    password = input("Enter your password: ")
    for user in user_storage.values():
        if user.username == user_email or user.email == user_email:
            if user.password == password:
                login = True
                print("Welcome!")
                return user
                # User gains access to their page
            else:
                print("Incorrect password, try again.")
                break
    if not login:
        print("No account found")
    return None
