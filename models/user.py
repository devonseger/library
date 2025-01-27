import json
from book import Book

class User:  # The class is a blueprint for creating objects (OOP), It defines properties and methods
    # User is the parent class
    def __init__(self, name, borrowed_books):  # init is the constructor, it is a method that is automatically called when an object of the class is created
        self.name = name  # A user object is created with the name and borrowed books properties
        self.borrowed_books = borrowed_books

    def view_borrowed_books():
        pass

    

    def __str__(self):
        book_list = "\n".join(str(book) for book in self.borrowed_books)
        return f"{self.name} currently has {len(self.borrowed_books)} book(s):\n{book_list}"
    
class Librarian(User):  # Librarian inherits from User therefor it's child class
    def __init__(self, name):
        super().__init__(name)  # super is used to call methods from the parent class

    def add_book(self, library, book):
        pass

    def remove_book(self, library, book):
        pass

