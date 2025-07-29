import json
from pathlib import Path


# Define where to store the books data
BOOKS_FILE = Path("data/books.json")

# Load the current books from the file, or create empty structure if the file doesn't exist
def load_books(file_path):
    if not BOOKS_FILE.exists() or BOOKS_FILE.stat().st_size == 0:
        return {"to_read": [], "completed": []}
    with open(BOOKS_FILE, "r") as file:
        return json.load(file)
        
    
# Save the current books data to the JSON file
def save_books(file_path, books):
    BOOKS_FILE.parent.mkdir(parents=True, exist_ok=True)    # Makes sure 'data/' exists
    with open(BOOKS_FILE, "w") as file:
        json.dump(books, file, indent=4)


# Example of how to use it 
if __name__ == "__main__":
    books = load_books()
    print("Books loaded successfully.")
    print(books)