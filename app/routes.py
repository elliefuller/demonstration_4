from flask import render_template
from . import app
from app.blueprints.books import books_blueprint

app.register_blueprint(books_blueprint, url_prefix='/books')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('books.html')

