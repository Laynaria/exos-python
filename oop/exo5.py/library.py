from book import Book

class Library:
    def __init__(self):
        self.books : list[Book] = []

    def add_book(self, new_book) -> None:
        self.books.append(new_book)
    
    def remove_book(self, book_to_remove: Book) -> None:
        if book_to_remove in self.books:
            self.books.remove(book_to_remove)
        else:
            print(f"The book {book_to_remove.title} isn't part of this library.")

    def show_books(self) -> None:
        for book in self.books:
            print(book)