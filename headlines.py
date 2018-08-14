import feedparser
from flask import Flask

app = Flask(__name__)

RSS_Feed = {'bbc_feed' : "http://feeds.bbci.co.uk/news/rss.xml",
            'cnn_feed' : "http://rss.cnn.com/rss/edition.rss",
            'fox_feed' : "http://feeds.foxnews.com/foxnews/latest"}

@app.route('/<publication>')
def get_news(publication="bbc"):

    publication = publication + '_feed'

    feed = feedparser.parse(RSS_Feed[publication])
    first_article = feed['entries'][0]

    return """<html>
            <body>
                <h1> BBC Headlines </h1>
                <b>{0}</b> <br/>
                <i>{1}</i> <br/>
                <p>{2}</p> <br/>
            </body>
        </html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=True)