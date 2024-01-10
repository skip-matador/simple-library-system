# main.py
from book import Book
from patron import Patron
from library_manager import LibraryManager

# Create books
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4")

# Create patrons
patron1 = Patron("Alice", "P001")
patron2 = Patron("Bob", "P002")

# Create a library manager
library_manager = LibraryManager()

# Add books and patrons to the library manager
library_manager.add_book(book1)
library_manager.add_book(book2)
library_manager.add_patron(patron1)
library_manager.add_patron(patron2)

# Display library information
library_manager.display_books()
library_manager.display_patrons()
