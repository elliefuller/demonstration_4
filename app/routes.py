from flask import render_template
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('books.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/events')
def events():
    return render_template('events.html')

