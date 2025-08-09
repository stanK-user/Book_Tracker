from flask import Flask, render_template, request, redirect, url_for
from books import add_book, mark_book_completed, remove_book, get_all_books
from datetime import datetime
import os


app = Flask(__name__)


@app.route("/")
def index():
    filter_by = request.args.get("filter")  # can be "completed", "to_read", or None
    sort_type = request.args.get('sort', '')
    books = get_all_books()

    if filter_by == "completed":
        books = [book for book in books if book.get("completed")]
    elif filter_by == "to_read":
        books = [book for book in books if not book.get("completed")]

    if sort_type == 'title_asc':
         books.sort(key=lambda b: b['title'].lower())
    elif sort_type == 'title_desc':
        books.sort(key=lambda b: b['title'].lower(), reverse=True)
    elif sort_type == 'author_asc':
        books.sort(key=lambda b: b['author'].lower())
    elif sort_type == 'author_desc':
        books.sort(key=lambda b: b['author'].lower(), reverse=True)
    elif sort_type == 'newest':
        books.sort(key=lambda b: datetime.fromisoformat(b['date_added']), reverse=True)
    elif sort_type == 'oldest':
        books.sort(key=lambda b: datetime.fromisoformat(b['date_added']))
    elif sort_type == 'completed_first':
        books.sort(key=lambda b: (not b['completed'], b['title'].lower()))
    elif sort_type == 'to_read_first':
        books.sort(key=lambda b: (b['completed'], b['title'].lower()))

    return render_template("index.html", books=books, filter=filter_by, sort=sort_type)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "")
    author = request.form.get("author", "")
    add_book(title, author)
    return redirect(url_for("index"))

@app.route("/mark_completed")
def mark_completed():
    title = request.args.get("title")
    author = request.args.get("author")
    mark_book_completed(title, author)
    return redirect(url_for("index"))

@app.route("/remove")
def remove():
    title = request.args.get("title")
    author = request.args.get("author")
    remove_book(title, author)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
