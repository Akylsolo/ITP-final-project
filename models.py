from datetime import datetime

class LibraryItem:
    def __init__(self, item_id, title):
        self._id = item_id
        self._title = title

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    def get_info(self):
        return f"{self._id}. {self._title}"

class Book(LibraryItem):
    def __init__(self, item_id, title, author, available=True):
        super().__init__(item_id, title)
        self.author = author
        self.available = available

    def get_info(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.id}. {self.title} by {self.author} - {status}"

class DigitalBook(Book):
    def __init__(self, item_id, title, author, file_format="PDF", available=True):
        super().__init__(item_id, title, author, available)
        self.file_format = file_format

    def get_info(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.id}. {self.title} by {self.author} [{self.file_format}] - {status}"

class User:
    def __init__(self, user_id, name, borrowed_books=None, history=None):
        self.user_id = user_id
        self.name = name
        self.borrowed_books = borrowed_books or []
        self.history = history or []

    def add_history(self, action):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"{current_time} - {action}")