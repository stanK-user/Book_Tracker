import json
from pathlib import Path
from config import FILE_PATH


# Load the current books from the file, or create empty structure if the file doesn't exist
def load_books():
    if not FILE_PATH.exists() or FILE_PATH.stat().st_size == 0:
        return {"to_read": [], "completed": []}
    with open(FILE_PATH, "r") as file:
        return json.load(file)
        
# Save the current books data to the JSON file
def save_books(books):
    FILE_PATH.parent.mkdir(parents=True, exist_ok=True)    # Makes sure 'data/' exists
    with open(FILE_PATH, "w") as file:
        json.dump(books, file, indent=4)