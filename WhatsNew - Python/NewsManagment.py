from datetime import datetime, timedelta, timezone
import requests
from dateutil import parser

api_key = "0412b9d965504b7880f90e1701042a37"
api_url = "https://newsapi.org/v2/everything?q=keyword&apiKey=0412b9d965504b7880f90e1701042a37"


class Article:
    def __init__(self, title, source, publishedAt, url, topic, author):
        self.title = title
        self.source = source
        self.publishedAt = publishedAt
        self.url = url
        self.topic = topic
        self.author = author
class NewsManager:
    def __init__(self):
        self.all_articles = []
    def fetch_articles(self, api_url,topic):
        headers = {
            "Authorization": f"Bearer {api_key}"
        }
        response = requests.get(api_url, headers=headers)
        data = response.json()
        for article_data in data.get("articles", []):
            published_at_dt = parser.isoparse(article_data["publishedAt"]).replace(tzinfo=timezone.utc)
            article = Article(
                    title=article_data.get("title", ""),
                    source=article_data.get("source", {}).get("name", ""),
                    publishedAt=published_at_dt,
                    url=article_data.get("url", ""),
                    topic= topic if topic else "",
                    author=article_data.get("author", "")
                )
            self.all_articles.append(article)
    def filter_topics(self, article_list, topics_to_filter):
        sorted_list = []
        for article in article_list:
            if article.topic in topics_to_filter:
                sorted_list.append(article)
        return sorted_list

    def filter_by_date(self, articles, time_range):
        now = datetime.now(timezone.utc)
        if time_range == "Last 24 hours":
            cutoff = now - timedelta(hours=24)
        elif time_range == "Past week":
            cutoff = now - timedelta(days=7)
        elif time_range == "Past month":
            cutoff = now - timedelta(days=30)
        elif time_range == "Past year":
            cutoff = now - timedelta(days=365)
        else:
            return articles
        return [a for a in articles if a.publishedAt >= cutoff]

    def sort_articles(self, user_list, sort_how, filter_date_bool, filter_date):
        if filter_date_bool:
            user_list = self.filter_by_date(user_list,filter_date)

        if sort_how == "A-Z":
            return sorted(user_list, key= lambda x: x.title)
        elif sort_how == "Z-A":
            return sorted(user_list, key= lambda x: x.title, reverse=True)

    def fetch_articles_by_preferences(self, user_list):
        user_topics = user_list
        for topic in user_topics:
            url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={api_key}"
            self.fetch_articles(url, topic)
