# ITP-final-project
# Library Management System

This project is a Python console application for managing books and users in a library.

## Features

- Show all books
- Show available books
- Show borrowed books
- Search books by title or author
- Borrow books
- Return books
- Track user history
- Show statistics
- Save and load data from JSON files

## Team Members

Maratov Nursultan: models.py and storage.py  
Muratbek Akyl: library.py  
Maksut Alibi: main.py, JSON files, README  

## How to Run
python test_library.py

##OOP Concepts
-The project uses classes such as LibraryItem, Book, DigitalBook, User, and Library.
-Inheritance is used because Book inherits from LibraryItem, and DigitalBook inherits from Book.
-Polymorphism is used because get_info() works differently in LibraryItem, Book, and DigitalBook.
-Encapsulation is used with _id and _title fields.

##Data Structures
-Dictionary is used for books and users because searching by ID is fast.
-List is used for borrowed books and history.
-JSON is used for permanent data storage.

##Advanced Python Features
-The project uses a decorator for logging successful operations.
-The project uses a generator to return books one by one.

##Testing
The project uses assert statements to test searching, statistics, available books, and invalid users.
