import json
from models.book import Book

class Library:
    def __init__(self):  # runs automatically when we create an instance
        print("You have created a library instance.")
        self.books = []

    def get_books(self, filename="books.json"):
        try:
            with open(filename, "r") as file:
                books = json.load(file)
            return [book["title"] for book in books]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def get_users(self):
        pass

    def find_book():
        pass

    def borrow_book(self, book):  # A method is a function defined inside of a class and is used to perform operations on objects of that class.
        if not book.checked_out:
            self.borrowed_books.append(book)  # Objects are automatically empty lists
            self.save_to_file()  # Create a new method below to save data to json file.

    def return_book(self, book):
        if book.checked_out:
            self.borrowed_books.remove(book)
            book.mark_as_returned()
            self.save_to_file()

    def save_to_file(self, filename="books.json"):
        try:
            with open(filename, "w") as file:
                book_data = [{"title": book.title, "author": book.author, "price": book.price, "published_date": book.published_date} for book in self.books]
                json.dump(book_data, file, indent=4)
        except Exception as e:
            print(f"Error saving books: {e}")