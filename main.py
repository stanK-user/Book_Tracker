# main.py

from books import add_to_read_books, add_to_completed_books, get_completed_books, get_to_read_books, mark_book_as_completed, remove_book

def print_books(books):
    if not books:
        print("  (No books found)")
    else:
        for i, book in enumerate(books, 1):
            title = book["title"]
            author = book["author"]
            print(f"  {i}. '{title}' by {author}")


def print_menu():
    print("\n📚 Book Tracker")
    print("1. Add a book to your 'to read' list")
    print("2. Add a book to your 'completed' list")
    print("3. View your 'to read' list")
    print("4. View your 'completed' list")
    print("5. Mark a book as completed")
    print("6. Remove a book")
    print("7. Exit")

def main():
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            add_to_read_books(title, author)

        elif choice == "2":
            title = input("Enter the book title: ")
            author = input("Enter the author: ")
            add_to_completed_books(title, author)

        elif choice == "3":
            print("\nYour 'to read' list:")
            to_read = get_to_read_books()
            print_books(to_read)

        elif choice == "4":
            print("\nYour 'completed' list")
            completed = get_completed_books()
            print_books(completed)

        elif choice == "5":
            to_read = get_to_read_books()
            print("\nYour 'to read' list:")
            print_books(to_read)
            if to_read:
                try:
                    book_num = int(input("Enter the number of the book to mark as completed:"))
                    mark_book_as_completed(book_num)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "6":
            print("\nRemove from:")
            print("  1. 'to read' list")
            print("  2. 'completed' list")
            list_choice = input("Choose list (1 or 2): ").strip()

            if list_choice == "1":
                book_list = get_to_read_books()
                list_name = "to_read"
            elif list_choice == "2":
                book_list = get_completed_books()
                list_name = "completed"
            else:
                print("Invalid choice.")
                continue

            print(f"\nYour '{list_name}' list:")
            print_books(book_list)

            if book_list:
                try:
                    book_num = int(input("Enter the number of the book to remove: "))
                    remove_book(list_name, book_num)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number 1 to 7.")

if __name__ == "__main__":
    main()
