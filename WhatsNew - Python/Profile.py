import os
import shutil
from NewsManagment import NewsManager
from Email_Maintance import send_verification_code
class Profile:
    def __init__(self, id, profile_pic = None,display_color = None):
        self.id = id
        self.display_color = display_color
        self.profile_pic = profile_pic
        self.article_preferences = []
        self.saved_articles = []
        self.new_manager = NewsManager()

    def change_email(self,cursor,conn):
        while True:
            new_email = input("Enter new email: ").strip()
            if "@" not in new_email or "." not in new_email:
                print("Invalid email")
                continue
            else:
                break
        code = send_verification_code(new_email)
        if not code:
            print("Failed to send verification email.")
            return
        while True:
            verification = input("Enter your verification code: ")
            if verification != code:
                print("Incorrect code, please try again")
            else:
                break
        sql = """ UPDATE "user" SET email = %s WHERE id = %s; """
        cursor.execute(sql,(new_email,self.id))
        conn.commit()
        print("Your email has changed")

    def change_password(self,cursor,conn):
        class InvalidPasswordChange(Exception):
            pass
        sql = """ SELECT email FROM "user" WHERE id = %s; """
        cursor.execute(sql,(self.id,))
        result = cursor.fetchone()
        user_db_email = result["email"]
        while True:
            email = input("Enter email: ")
            if user_db_email != email:
                print("Incorrect email please try again")
                continue
            else:
                code = send_verification_code(email)
                print("A code was sent to your email for verification.")
                verify_code = input("Please input the code: ")
                if verify_code != code:
                    print("Incorrect code, please try again")
                else:
                    break
        while True:
            try:
                new_password = input("Enter new password: ")
                if len(new_password) < 8 or len(new_password) > 32:
                    raise InvalidPasswordChange("Password must be 8-32 characters")
                elif not any(char.isupper() for char in new_password) or not any(char.islower() for char in new_password):
                    raise InvalidPasswordChange("Must contain at least must 1 upper case and 1 lowercase letter")
                elif not any(char.isdigit() for char in new_password):
                    raise InvalidPasswordChange("Must have at least one digit in your password")
                else:
                    sql = """UPDATE "user" SET password = %s WHERE id = %s;"""
                    cursor.execute(sql,(new_password,self.id))
                    conn.commit()
                    print("Your password has changed.")
                    break
            except InvalidPasswordChange as e:
                print(e)
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

    def change_username(self):
        pass

    def delete_profile(self):
        pass
