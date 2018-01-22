from flask import render_template
from app import app
from .request import get_movies

# Views


@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')

    # message = 'Mans not hot'
    title = "Home - Welcome to The Best Movie Review Website Online"
    return render_template('index.html',
                           title=title,
                           popular=popular_movies,
                           upcoming=upcoming_movies,
                           now_showing=now_showing_movies)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    """
    This is the movie route and function that is meant to return
    -movie details page and its data

    By default dynamic parts are rendered as strings but
    they can be transformed to be any type.
    Eg above we want the movie id to be a number
    """
    # movie_id = "7890" This would set an unchangeble movie_id
    return render_template('movie.html', id=movie_id)
