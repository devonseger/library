import uuid

class Book:
    
    def __init__(self,title,author,price,published_date):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.price = price
        self.published_date = published_date
        self.checked_out = False

    def mark_as_borrowed(self):
        if self.checked_out:
            print(f"Sorry {self.title} is already checked out!")
        else:
            self.checked_out = True

    def mark_as_returned(self):
        if self.checked_out:
            self.checked_out = False
        else:
            print(f"{self.title} is not checked out!")


    def __str__(self):
        return(f"{self.title}, by {self.author}, Price: ${self.price}, Published: {self.published_date}")