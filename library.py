from models import Book, User
from storage import load_json, save_json
class Library:
    def __init__(self, books_file="books.json", users_file="users.json"):
        self.books_file = books_file
        self.users_file = users_file
        self.books = self.load_books()
        self.users = self.load_users()
    def load_books(self):
        data = load_json(self.books_file)
        return {
            book["id"]: Book(
                book["id"],
                book["title"],
                book["author"],
                book["available"]
            )
            for book in data
        }
    def load_users(self):
        data = load_json(self.users_file)
        return {
            user["user_id"]: User(
                user["user_id"],
                user["name"],
                user.get("borrowed_books", []),
                user.get("history", [])
            )
            for user in data
        }
    def save_data(self):
        books_data = [
            {
                "id": b.id,
                "title": b.title,
                "author": b.author,
                "available": b.available
            }
            for b in self.books.values()
        ]
        users_data = [
            {
                "user_id": u.user_id,
                "name": u.name,
                "borrowed_books": u.borrowed_books,
                "history": u.history
            }
            for u in self.users.values()
        ]
        save_json(self.books_file, books_data)
        save_json(self.users_file, users_data)
    def borrow_book(self, user_id, book_id):
        if user_id not in self.users:
            raise ValueError("User not found")
        if book_id not in self.books:
            raise ValueError("Book not found")
        user = self.users[user_id]
        book = self.books[book_id]
        if not book.available:
            raise ValueError("Book is not available")
        if book_id in user.borrowed_books:
            raise ValueError("User already borrowed this book")
        book.available = False
        user.borrowed_books.append(book_id)
        user.history.append(f"Borrowed book: {book.title}")
        self.save_data()
    def return_book(self, user_id, book_id):
        if user_id not in self.users:
            raise ValueError("User not found")

        if book_id not in self.books:
            raise ValueError("Book not found")
        user = self.users[user_id]
        book = self.books[book_id]
        if book_id not in user.borrowed_books:
            raise ValueError("This user did not borrow this book")
        book.available = True
        user.borrowed_books.remove(book_id)
        user.history.append(f"Returned book: {book.title}")
        self.save_data()
    def get_available_books(self):
        return [book for book in self.books.values() if book.available]
    def get_all_books(self):
        return list(self.books.values())
    def book_generator(self):
        for book in self.books.values():
            yield book

    def search_books(self, keyword):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower() or keyword in book.author.lower()
        ]

    def get_borrowed_books(self):
        return [book for book in self.books.values() if not book.available]

    def get_user_history(self, user_id):
        if user_id not in self.users:
            raise ValueError("User not found")
        return self.users[user_id].history

    def get_statistics(self):
        total_books = len(self.books)
        available_books = len(self.get_available_books())
        borrowed_books = total_books - available_books
        total_users = len(self.users)

        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_users": total_users
        }