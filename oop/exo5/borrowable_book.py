from book import Book

class BorrowableBook(Book):
    def __init__(self, title, author, publication_year):
        super().__init__(title, author, publication_year)
        self.available = True

    @property
    def available(self) -> bool:
        return self.__available

    @available.setter
    def available(self, new_availability):
        self.__available = new_availability

    def show_details(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Year: {self.publication_year}")
        print(f"Available: {"Available" if self.available else "Already Borrowed"}")

# We could skip setter to protect it more, and only add the borrow and give back methods here instead of in library
# It could be better for purposes to have the borrowable methods here in, for best practics of separation of concerns