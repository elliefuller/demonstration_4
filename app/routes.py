from flask import render_template
from . import app
from app.db_connect import get_db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/reads')
def reads():
    return render_template('reads.html')

@app.route('/authors')
def authors():
    return render_template('authors.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/books')
def books():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM books')
    all_books = cursor.fetchall()
    return render_template('books.html')