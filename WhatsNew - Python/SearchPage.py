from NewsManagment import NewsManager
from Login import user
manager = NewsManager()
search = input("What would you like to find?: ").split()
articles = manager.fetch_articles_by_preferences(search)

for num, article in enumerate(articles, start=1):
    print(f"{num}. {article.title}")


choice = int(input("Enter the number of the article to remove (0 to cancel): "))
if choice != 0 and 1 <= choice <= len(user.profile.saved_article):
    del user.profile.saved_article[choice - 1]
