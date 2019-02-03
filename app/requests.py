import urllib.request,json
from .models import News
# import time

# now=time.strftime("%c")
#Getting api key
api_key=None
base_url=None

def configure_request(app):
    global api_key,base_url
    api_key=app.config['NEWS_API_KEY']
    base_url=app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response= json.loads(get_news_data)

        news_results = None
        if get_news_response['articles']:
            news_articles_list = get_news_response['articles']
            news_articles = process_articles(news_articles_list)
    return news_articles

def process_articles(news_list):
    '''
    Function that processes the news result and transform them to a list of Objects

    Args:
        news_list: A list of dictionaries that contain news details

    Returns :
        news_articles: A list of news objects
    '''
    news_articles = []
    for news_article in news_list:
        source = news_article.get('source')
        source_name = source.get('name')
        source_url= news_article.get('url')
        author_name=news_article.get('author')
        imageUrl= news_article.get('urlToImage')
        description=news_article.get('description')
        article=news_article.get('content')
        timeOfCreation=news_article.get('publishedAt')
        news_article = News(source_name,source_url,author_name,imageUrl,description,article,timeOfCreation)
        news_articles.append(news_article)

    return news_articles
