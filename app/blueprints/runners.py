from flask import Blueprint, render_template, request, url_for, redirect, flash
from app.db_connect import get_db

book_info = Blueprint('book_info', __name__)

@book_info.route('/books', methods=['GET', 'POST'])
def books():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new book
    if request.method == 'POST':
        book_title = request.form['book_title']
        book_author = request.form['book_author']
        book_genre = request.form['book_genre']
        book_pages = request.form['book_pages']

        # Insert the new book into the database
        cursor.execute('INSERT INTO book_info (book_title, book_author, book_genre, book_pages) VALUES (%s, %s, %s, %s)',
                       (book_title, book_author, book_genre, book_pages))
        db.commit()

        flash('New book added successfully!', 'success')
        return redirect(url_for('book_info.books'))

    # Handle GET request to display all books
    cursor.execute('SELECT * FROM book_info')
    all_books = cursor.fetchall()
    return render_template('books.html', all_books=all_books)

@book_info.route('/update_book/<int:book_id>', methods=['GET', 'POST'])
def update_book(book_id):
    db = get_db()
    cursor = db.cursor()

    if request.method == 'POST':
        # Update the book's details
        book_title = request.form['book_title']
        book_author = request.form['book_author']
        book_genre = request.form['book_genre']
        book_pages = request.form['book_pages']

        cursor.execute('UPDATE book_info SET book_title = %s, book_author = %s, book_genre = %s, book_pages = %s WHERE book_id = %s',
                       (book_title, book_author, book_genre, book_pages, book_id))
        db.commit()

        flash('Book updated successfully!', 'success')
        return redirect(url_for('book_info.books'))

    # GET method: fetch book's current data for pre-populating the form
    cursor.execute('SELECT * FROM book_info WHERE book_id = %s', (book_id,))
    book = cursor.fetchone()
    return render_template('update_book.html', book=book)

@book_info.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the book
    cursor.execute('DELETE FROM book_info WHERE book_id = %s', (book_id,))
    db.commit()

    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('book_info.books'))
