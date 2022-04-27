from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
    
@app.route("/movies")
def movies():
    """Movies Page"""
    return render_template("movies.html")



