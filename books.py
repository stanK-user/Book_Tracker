from storage import load_books, save_books
from datetime import datetime

def add_book(title, author):
    books = load_books()
    
    # Check for duplicates
    for book in books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            print("Book already exists.")
            return

    new_book = {
        "title": title.strip(),
        "author": author.strip(),
        "completed": False,
        "added": datetime.now().isoformat()
    }

    books.append(new_book)
    save_books(books)
    print(f"Added: {title} by {author}")


def mark_book_completed(title, author):
    books = load_books()
    updated = False

    for book in books:
        if book["title"].lower() == title.lower() and book["author"].lower() == author.lower():
            if book["completed"]:
                print("Book already marked as completed.")
            else:
                book["completed"] = True
                updated = True
                print(f"Marked as completed: {title} by {author}")
            break
    else:
        print("Book not found.")

    if updated:
        save_books(books)

def get_all_books():
    books = load_books()
    if not books:
        print("No books found.")
        return

    print("\nYour Books:")
    for book in books:
        status = "✅ Completed" if book["completed"] else "📖 To Read"
        print(f"- {book['title']} by {book['author']} ({status})")


def remove_book(title, author):
    title = title.strip().lower()
    author = author.strip().lower()

    books = load_books()
    initial_count = len(books)

    # Filter out any book matching both title and author
    books = [
        book for book in books
        if not (book["title"].lower() == title and book["author"].lower() == author)
    ]

    if len(books) < initial_count:
        save_books(books)
        print(f"Removed '{title.title()}' by {author.title()} from your list.")
    else:
        print(f"Book '{title.title()}' by {author.title()} not found in your list.")