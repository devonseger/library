import json
from book import Book

class Library:

    def get_books(self):
        pass

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

    def save_to_file(self, filename="users.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}  # empty dict if file not found

        data[self.name] = [book.title for book in self.borrowed_books]

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)