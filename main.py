# main.py

from books import add_book, mark_book_completed, get_all_books

def main():
    while True:
        print("\nBook Tracker Options:")
        print("1. Add Book")
        print("2. Mark Book as Completed")
        print("3. View All Books")
        print("4. Quit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            add_book(title, author)

        elif choice == "2":
            title = input("Title to mark as completed: ")
            author = input("Author: ")
            mark_book_completed(title, author)

        elif choice == "3":
            get_all_books()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
