import random
import os
import shutil

class Profile:
    def __init__(self, username, email, password, id, profile_pic, saved_article,display_color = None, newUser = True):
        self.username = username
        self.email = email
        self.password = password
        self.id = id
        self.newUser = newUser
        self.display_color = display_color
        self.profile_pic = profile_pic
        self.article_preferences = []
        self.saved_article = []

    def change_email(self):
        class InvalidEmailException(Exception):
            pass
        new_email = input("Enter new email: ")
        verify_code = str(random.randint(00000,99999))
        # here is where the code is sent to the email
        attempts = 5
        while attempts != 0:
            try:
                print("A code was sent to your email for verification.")
                verify_email = input("Please input the code: ")
                if verify_code != verify_email:
                    raise InvalidEmailException("Wrong code, please try again")
                # Option to resend the code here
                else:
                    self.email = new_email
            except InvalidEmailException as e:
                print(e)
        print("Too many failed attempts, can no longer change email for 14 days.")
        # Find a way to make the function inaccessible

    def change_password(self):
        class InvalidPasswordChange(Exception):
            pass
        email = input("Enter email: ")
        verify_code = str(random.randint(00000, 99999))
        # send code to User
        attempts = 5
        while attempts != 0:
            try:
                print("A code was sent to your email for verification.")
                verify_email = input("Please input the code: ")
                if verify_code != verify_email:
                    raise InvalidPasswordChange("Wrong code, please try again")
                # Option to resend the code here
                else:
                    new_password = input("Enter new password: ")
                    if len(new_password) < 8 or len(new_password) > 32:
                        raise InvalidPasswordChange("Password must be 8-32 characters")
                    elif not any(new_password.upper() for char in new_password) or not any(new_password.lower() for char in new_password):
                        raise InvalidPasswordChange("Must contain at least must 1 upper case and 1 lowercase letter")
                    elif not any(char.isdigit() for char in new_password):
                        raise InvalidPasswordChange("Must have at least one digit in your password")
                    else:
                        self.password = new_password
            except InvalidPasswordChange as e:
                print(e)
        print("Too many failed attempts, can no longer change password for 14 days.")
        # Find a way to make the function inaccessible

    def profile_pic(self):
        profile_pic_folder = "profile pics"
        if not os.path.exists(profile_pic_folder):
            os.makedirs(profile_pic_folder)
        file_path = input("Path for profile pic: ").strip()
        if os.path.exists(file_path):
            print("Path does not exist")
            return
        file_ext = os.path.splitext(file_path)[1]
        user_pic = self.id + file_ext
        destination_path = os.path.join(profile_pic_folder,user_pic)
        shutil.copy(user_pic,destination_path)
        self.profile_pic = user_pic

    def change_display_color(self):
        pass
    def change_article_preference(self):
        print("Available topics: tech fashion sports music politics health science ")
        select_topics = input("What topics would you like to see? ").lower()
        self.article_preferences = select_topics.split(" ")
        # Change the user's article preferences