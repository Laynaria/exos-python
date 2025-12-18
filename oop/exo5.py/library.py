from borrowable_book import BorrowableBook

class Library:
    def __init__(self):
        self.books : list[BorrowableBook] = []

    def add_book(self, new_book) -> None:
        self.books.append(new_book)
    
    def remove_book(self, book_to_remove: BorrowableBook.title) -> None:
        for book in self.books:
            if book.title == book_to_remove :
                self.books.remove(book)
            else:
                print(f"The book {book_to_remove.title} isn't part of this library.")

    def show_books(self) -> None:
        for book in self.books:
            print(book)

    def borrow_book(self, title) -> None:
        for book in self.books:
            if (book.title == title and isinstance(book, BorrowableBook) and book.available):
                book.available = False
                print(f"You borrowed {book.title}")
                return
            
            if (book.title == title and isinstance(book, BorrowableBook) and book.available == False):
                print(f"{book.title} can't be borrowed!")
                return
    
    def return_book(self, title) -> None:
        for book in self.books:
            if (book.title == title and isinstance(book, BorrowableBook) and book.available == False):
                book.available = True
                print(f"You returned {book.title}")
                return
            
            if (book.title == title and isinstance(book, BorrowableBook) and book.available):
                print(f"{book.title} can't be returned!")
                return
    
    def load_library(self) -> None:
        pass

    def save_library(self) -> None:
        pass