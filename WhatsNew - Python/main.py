import Login
import Profile
import Homepage
import SavedArticlesPage
import SavedArticlesPage
import NewsManagment
if __name__ == "__main__":
    print("Welcome!")
    login = input("Do you have an account? ").lower()
    if login == "no":
        Login.login()
    else:
        Login.createaccount()