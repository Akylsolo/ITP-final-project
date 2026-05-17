from library import Library

def show_menu():
    print("\nLibrary Management System")
    print("1. Show all books")
    print("2. Show available books")
    print("3. Show borrowed books")
    print("4. Search book")
    print("5. Borrow book")
    print("6. Return book")
    print("7. Show user history")
    print("8. Show statistics")
    print("9. Exit")
def print_books(books):
    if not books:
        print("No books found")
        return
    for book in books:
        print(book.get_info())

def main():
    library = Library()
    while True:
        show_menu()
        choice = input("Choose option: ")
        try:
            if choice == "1":
                print_books(library.book_generator())
            elif choice == "2":
                print_books(library.get_available_books())
            elif choice == "3":
                print_books(library.get_borrowed_books())
            elif choice == "4":
                keyword = input("Enter title or author: ")
                print_books(library.search_books(keyword))
            elif choice == "5":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                library.borrow_book(user_id, book_id)
            elif choice == "6":
                user_id = int(input("Enter user ID: "))
                book_id = int(input("Enter book ID: "))
                library.return_book(user_id, book_id)
            elif choice == "7":
                user_id = int(input("Enter user ID: "))
                history = library.get_user_history(user_id)
                if not history:
                    print("History is empty")
                else:
                    for record in history:
                        print(record)
            elif choice == "8":
                statistics = library.get_statistics()
                for key, value in statistics.items():
                    print(f"{key}: {value}")
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid option")
        except ValueError as error:
            print("Error:", error)

if __name__ == "__main__":
    main()