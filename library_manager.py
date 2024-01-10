# library_manager.py
from book import Book
from patron import Patron

class LibraryManager:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def add_patron(self, patron):
        self.patrons.append(patron)

    def display_books(self):
        print("Library Books:")
        for book in self.books:
            book.display()

    def display_patrons(self):
        print("Library Patrons:")
        for patron in self.patrons:
            patron.display()
