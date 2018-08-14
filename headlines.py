import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)

RSS_Feeds = {'bbc' : "http://feeds.bbci.co.uk/news/rss.xml",
            'cnn' : "http://rss.cnn.com/rss/edition.rss",
            'fox' : "http://feeds.foxnews.com/foxnews/latest"}

@app.route('/')
def index():
    return "To view headlines, please go to http://localhost/bbc"

@app.route('/search')
def get_news():

    pub = request.args.get('pub')
    print pub
    if not pub or pub.lower() not in RSS_Feeds:
        publication = 'bbc'
    else:
        publication = pub.lower()

    print 'pub : ' + publication

    feed = feedparser.parse(RSS_Feeds[publication])
    #first_article = feed['entries'][0]
    articles = feed['entries']

    return render_template('news.html', articles=articles, publication=publication)
       # </html>.format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))

if __name__ == "__main__":
  app.run(port=5000, debug=True)