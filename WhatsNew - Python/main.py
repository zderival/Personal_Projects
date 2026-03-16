import Login
import NewsManagment
from Login import User
import Profile
import Homepage
import SavedArticlesPage
from NewsManagment import NewsManager, api_url2

if __name__ == "__main__":
    while True:
        choice = 0
        try:
            choice = int(input("Type 1 to Login, 2 to Create an Account: "))
        except ValueError:
            print("Invalid input please try again")
            continue
        if choice == 1:
            user: User = Login.login()
            if user is None:
                continue
        elif choice == 2:
            Login.create_account()
            continue
        else:
            print("Please type 1 or 2.")
            continue
        break

    print("Here is the latest news: ")
    articles = NewsManagment.print_article(api_url2)

    #Spesfiy what articles user want to see:
    # while True:
    #     print("Menu")
    #     print("What would you like to do")
    #     print("1) Find specific articles")
    #     print("2) Save articles")
    #     print("3) Search articles")
    #     print("")
    #     break

    #filter by topics function
    # preferences = input("What types of articles do you wish to see: ").lower().strip().split()
    # user.profile.article_preferences = preferences
    # user.profile.new_manager.filter_topics(user.profile.article_preferences)

    # Save/remove articles:
    # save_article_choice = [int(x) for x in input("Any articles you wish to save?: ").strip().split()]
    # user.profile.new_manager.save_articles(save_article_choice,user)
    # for i, article in enumerate(user.profile.saved_articles, start=1):
    #     print(f"{i}. {article}")
    #
    # save_article_choice = input("Any articles you wish to remove?: ").strip().split()
    # user.profile.new_manager.remove_articles(save_article_choice,user)
    # for i, article in enumerate(user.profile.saved_articles, start=1):
    #     print(f"{i}. {article}")

    # Search for articles
    # search = input("What would you like to find? ")
    # user.profile.new_manager.search_articles(search)
