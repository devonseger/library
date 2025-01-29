from models.book import Book
from models.user import User, Librarian
from models.library import Library

def main_menu():  # Defines a main menu, prints options and takes an input then returns that input as choice
    print("\nLibrary Management System")
    print("1. Add Book to Library.")
    print("2. Remove Book from Library.")
    print("3. View Books in Library.")
    print("4. View All Users.")
    choice = input("Enter choice: ")
    return choice

def main():
    # init library
    library = Library()
    user = User("Admin")
    librarian = Librarian("Admin")

    while True:
        choice = main_menu()
        if choice == "1":
            add_book_menu(librarian, library)
        if choice == "2":
            remove_book_menu(librarian)
        if choice == "3":
            print("Viewing all books")
            all_books = library.get_books()
            print("Books:", all_books)
        if choice == "4":
            print("Viewing all users")
            # make a function to view all users in db
        if choice == "exit":
            break
        

def add_book_menu(librarian, library):
    while True:
        print("Adding a book")
        title = input("\nPlease enter the title: ")
        author = input("\nPlease enter the Author: ")
        price = input("\nPlease enter the price of the book: ")
        published_date = input("\nPlease enter the published date: ")
        if title and price and published_date and author:
            if confirm_title(title, author, price, published_date) == 1:
                new_book = Book(title, author, price, published_date)
                librarian.add_book(library, new_book)
                break
            else:
                print("Please try again.")

def remove_book_menu(librarian):
    while True:
        t = input("Enter the title of the book you want to remove: ")
        if t:
            if confirm_title(t) == 1:
                # add logic to delete book from db
                break
            else:
                print("Please try again.")

def confirm_title(title, author, price, published_date):
    while True:
        try:
            c = input(f"You have entered '{title} by {author}, published on {published_date}, with an MSPR of ${price}', please enter 1 to confirm or 2 to edit: ")
            if c in ["1", "2"]:
                return int(c)
            else:
                print("Invalid input. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")


if __name__ == "__main__":
    main()