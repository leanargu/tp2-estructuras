import feedparser

feed = feedparser.parse("https://www.clarin.com/rss/lo-ultimo/")

print(feed)