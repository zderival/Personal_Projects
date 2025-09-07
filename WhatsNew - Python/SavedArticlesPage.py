import Login
from NewsManagment import NewsManager
manager = NewsManager()
user = Login.login()
for num, article in enumerate(user.profile.saved_article, start=1):
    print(f"{num}. {article.title}")

choice = int(input("Enter the number of the article to remove (0 to cancel): "))
if choice != 0 and 1 <= choice <= len(user.profile.saved_article):
    del user.profile.saved_article[choice - 1]

# Icon for sorting
sort_how = input("How do you want your list sorted? ")
filter_date_bool = False
filter_date = input("Do you want the dates filter (YES OR NO)? ").upper()
option = ""
if filter_date == "YES":
    filter_date_bool = True
    print("Last 24 hours")
    print("Past week")
    print("Past month")
    print("Past year")
    option = input("Select an option: ")
sort = manager.sort_articles(user.profile.saved_article, sort_how, filter_date_bool, option)
for num, article in enumerate(sort, start=1):
    print(f"{num}. {article.title}")
