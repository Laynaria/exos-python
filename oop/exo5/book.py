class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    # Getters / Setters
    @property
    def title(self) -> int:
        return self._title
    
    @title.setter
    def title(self, new_title) -> None:
        self._title = new_title

    @property
    def author(self) -> int:
        return self._author
    
    @author.setter
    def author(self, new_author) -> None:
        self._author = new_author

    @property
    def publication_year(self) -> int:
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, new_publication_year) -> None:
        self._publication_year = new_publication_year


    # Methods
    def show_details(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Year: {self.publication_year}")

    # Magic Methods
    def __str__(self):
        return f"Book : {self.title} written by {self.author} published in {self.publication_year}"

