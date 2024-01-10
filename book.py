# book.py

class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}")
