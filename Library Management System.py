# Library Management System

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def display_info(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {status}")
        print("-" * 30)


class Library:
    def __init__(self):
        self.books = []

    # Add a Book
    def add_book(self, title, author):
        if not title or not author:
            print("Error: Title and author cannot be empty.")
            return

        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book: {title} by {author} added to the library.")

    # View All Books
    def view_books(self):
        if not self.books:
            print("No books in the library.")
            return

        print("\n--- Library Catalog ---")
        for book in self.books:
            book.display_info()

    # Borrow a Book
    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"Book '{book.title}' has been borrowed. Enjoy reading!")
                else:
                    print(f"Book '{book.title}' is already borrowed.")
                return

        print(f"Book '{title}' was not found in the library.")

    # Return a Book
    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.is_borrowed:
                    book.is_borrowed = False
                    print(f"Book '{book.title}' has been returned successfully.")
                else:
                    print(f"Book '{book.title}' was not borrowed.")
                return

        print(f"Book '{title}' was not found in the library.")


# Main Program
library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        library.add_book(title, author)

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        title = input("Enter Book Title to borrow: ").strip()
        library.borrow_book(title)

    elif choice == "4":
        title = input("Enter Book Title to return: ").strip()
        library.return_book(title)

    elif choice == "5":
        print("Exiting the Library Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option (1-5).")



