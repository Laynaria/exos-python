from book import Book
from library import Library

new_library = Library()

new_book1 = Book("Gulliver's Travels", "Jonathan Swift", 1726)
new_book2 = Book("The Imaginary Invalid", "Molière", 1913)

print("Add first book :")
new_library.add_book(new_book1)
new_library.show_books()

print("Add second book :")
new_library.add_book(new_book2)
new_library.show_books()

print("Remove first book: ")
new_library.remove_book(new_book1)
new_library.show_books()