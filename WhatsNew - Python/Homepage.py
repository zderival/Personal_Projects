import Login
from NewsManagment import NewsManager
from Login import temp_id_storage
manager = NewsManager()
user = Login.login()
# Fetch recommended articles
for user in list(temp_id_storage.values()):
    if user.newUser:
        # Ask this user what their topics will be and the screen shown here
        preferences = input("What types of articles do you wish to see: ")
        user_preferences = preferences.lower().split(" ")
        user.profile.article_preferences = user_preferences

        user.newUser = False
        del temp_id_storage[user]
    else:
        del temp_id_storage[user]
manager.fetch_articles_by_preferences(user.profile.article_preferences)
print("Recommended Articles")
for num, article in enumerate(manager.all_articles, start=1):
    print(f"{num}. {article.title}")

choice = input("Options: Save article, Remove saved article, Back to main menu: ").upper()
if choice == "Save article":
    article_num = int(input("Enter the number of the article to save: "))
    if 1 <= article_num <= len(manager.all_articles):
        user.profile.saved_article.append(manager.all_articles[article_num - 1])
elif choice == "Remove saved article":
    saved_articles(user)


