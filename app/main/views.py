from flask import render_template, request, redirect, url_for
from . import main
from ..requests import get_news
# , get_a_news, search_news

@main.route('/')

def index():

    '''
    This view function returns the index page and its data
    '''
    todays_highlights = get_news("general")
    todays_weather = get_news('weather')
    todays_sports = get_news('sports')

    title = 'Home - Welcoome to the best NEWS UPDATES online site'
    # search_news = request.args.get('news_query')
    # if search_movie:
    #     return redirect(url_for('main.search',movie_name = search_news))
    # else
    return render_template('index.html',title=title,general=todays_highlights ,weather=todays_weather,sports=todays_sports)
# search_news = request.args.get('news_query')
    # if search_movie:
    #     return redirect(url_for('main.search',movie_name = search_news))
    # else# search_news = request.args.get('news_query')
    # if search_movie:
    #     return redirect(url_for('main.search',movie_name = search_news))
    # else
