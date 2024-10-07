from flask import render_template
from . import app
from app.blueprints.book_info import book_info

app.register_blueprint(book_info, url_prefix='/book_info')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/books')
def books():
    return render_template('books.html')

