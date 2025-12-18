from borrowable_book import BorrowableBook
from library import Library

new_library = Library()

while True:
    print("\nMenu")
    print("1. Add A Book")
    print("2. Remove a Book")
    print("3. Show List of Books")
    print("4. Borrow a Book")
    print("5. Return a Book")
    print("6. Search for a Book")
    print("7. Exit Library")

    choix = input("\nWhat do you want to do ? ")

    match choix:
        case "1":
            title = input("Book Title: ")
            author = input("Author Name: ")
            publication_year = input("Published in: ")
            
            book = BorrowableBook(title, author, publication_year)
            new_library.add_book(book)
            print(f"{title} successfully added to the Library")

        case "2":
            title = input("\nBook you want to remove: ")
            new_library.remove_book(title)
            print(f"{title} successfully removed from Library")
        
        case "3":
            print("\nList of Library's books")
            new_library.show_books()
        
        case "4":
            title = input("\nBook you want to borrow: ")
            new_library.borrow_book(title)

        case "5":
            title = input("\nBook you want to return: ")
            new_library.return_book(title)

        case "6":
            title = input("\nBook you want to search: ")
            for book in new_library.books:
                if book.title == title:
                    book.show_details()
                    break
            else:
                print(f"No book with this title!")


        case "7":
            print("Goodbye!")
            break