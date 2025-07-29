import json
from pathlib import Path
from datetime import datetime
from storage import load_books, save_books


def add_to_read_books(title, author):
    title = title.strip()
    author =  author.strip()

    if not title or not author:
        print("Error: Title and author cannot be empty.")
        return
    
    books = load_books()

    # Check duplicates in "to_read"
    for book in books["to_read"]:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("This book is already in your 'to read' list.")
            return

    # Add book with timestamp
    new_book = {
        "title": title,
        "author": author,
        "added": datetime.now().isoformat()
    }
    books["to_read"].append(new_book)
    save_books(books)
    print(f"Added '{title}' by {author} to your 'to read' list")


def add_to_completed_books(title, author):
    title = title.strip()
    author = author.strip()

    if not title or not author:
        print("Error: Title and author cannot be empty.")
        return
    
    books = load_books()

    # Check duplicates in "completed"
    for book in books["completed"]:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("This book is already in your 'completed' list.")
            return
        
    # Add book with timestamp
    new_book = {
        "title": title,
        "author": author,
        "date_completed": datetime.now().isoformat()
    }
    books["completed"].append(new_book)
    save_books(books)
    print(f"Added '{title}' by {author} to your 'completed' list")


def get_to_read_books(file_path=None):
    books = load_books(file_path)
    return books["to_read"]

def get_completed_books(file_path=None):
    books = load_books(file_path)
    return books["completed"]


def mark_book_as_completed(index, file_path=None):
    books = load_books(file_path)
    to_read = books["to_read"]

    if index < 1 or index > len(to_read):
        print("Invalid book number.")
        return

    book = to_read.pop(index - 1)  # remove from to_read

    book["date_completed"] = datetime.now().isoformat()
    books["completed"].append(book)

    save_books(books, file_path)
    print(f"Marked '{book['title']}' by {book['author']}' as completed.")


def remove_book(list_name, index, file_path=None):
    books = load_books(file_path)
    book_list = books[list_name]

    if index < 1 or index > len(book_list):
        print("Invalid book number.")
        return

    book = book_list.pop(index - 1)
    save_books(books, file_path)
    print(f"Removed '{book['title']}' by {book['author']}' from '{list_name}' list.")
