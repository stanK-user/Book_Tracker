import json
from pathlib import Path
from datetime import datetime


# Define where to store the books data
BOOKS_FILE = Path("data/books.json")

# Load the current books from the file, or create empty structure if the file doesn't exist
def load_books():
    if not BOOKS_FILE.exists() or BOOKS_FILE.stat().st_size == 0:
        return {"to_read": [], "read": []}
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)
        
    
# Save the current books data to the JSON file
def save_books(books):
    BOOKS_FILE.parent.mkdir(parents=True, exist_ok=True)    # Makes sure 'data/' exists
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)


# Example of how to use it 
if __name__ == "__main__":
    books = load_books()
    print("Books loaded successfully.")
    print(books)


def add_to_read_books(title, author)
    title = title.strip()
    author =  author.strip()

    if not title or not author:
        print("Error: Title and author cannot be empty.")
        return
    
    books = load_books

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