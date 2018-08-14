import feedparser
from flask import Flask, render_template

app = Flask(__name__)

RSS_Feed = {'bbc_feed' : "http://feeds.bbci.co.uk/news/rss.xml",
            'cnn_feed' : "http://rss.cnn.com/rss/edition.rss",
            'fox_feed' : "http://feeds.foxnews.com/foxnews/latest"}

@app.route('/')
def index():
    return "To view headlines, please go to http://localhost/bbc"

@app.route('/<publication>')
def get_news(publication="bbc"):

    publication = publication + '_feed'

    feed = feedparser.parse(RSS_Feed[publication])
    #first_article = feed['entries'][0]
    articles = feed['entries']

    return render_template('news.html', articles=articles)
       # </html>.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=True)