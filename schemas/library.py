from db.session import get_session
from schemas.book import Book, BookStatus


class Library:
    """Class representing the library."""

    def __init__(self):
        self.books = []
        self.load_books()
        self.primary_key = len(self.books)

    def load_books(self):
        """Load books from the JSON database."""
        with get_session() as session:
            self.books = [
                Book(
                    book["id"],
                    book["title"],
                    book["author"],
                    book["year"],
                    BookStatus(book["status"]),
                )
                for book in session
            ]

    def save_books(self):
        """Save books to the JSON database."""
        with get_session() as session:
            session.clear()
            session.extend([book.__dict__ for book in self.books])

    def add_book(self, title: str, author: str, year: int):
        """Add a book to the library with a unique ID and initial status 'in_stock'."""
        self.primary_key += 1
        book_id = self.primary_key
        new_book = Book(book_id, title, author, year, BookStatus.IN_STOCK)
        self.books.append(new_book)
        self.save_books()

    def remove_book(self, book_id: int):
        book_to_remove = next((book for book in self.books if book.id == book_id), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
        else:
            print(f"Error: Book with ID {book_id} not found.")

    def search_books(self, search_type: str, query: str):
        """Search for books based on the specified parameter."""
        found_books = []

        if search_type == "id":
            if query.isdigit():
                book_id = int(query)
                found_books = [book for book in self.books if book.id == book_id]
            else:
                print("Error: ID must be an integer.")
        elif search_type == "year":
            if query.isdigit():
                year = int(query)
                found_books = [book for book in self.books if book.year == year]
            else:
                print("Error: Year must be an integer.")
        elif search_type == "title":
            found_books = [
                book for book in self.books if query.lower() in book.title.lower()
            ]
        elif search_type == "author":
            found_books = [
                book for book in self.books if query.lower() in book.author.lower()
            ]
        else:
            print(
                "Error: Invalid search type. Choose from 'id', 'year', 'title', or 'author'."
            )

        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"No books found for query: {query}")

    def list_books(self):
        """Display all books in the library."""
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books available in the library.")

    def change_status(self, book_id: int, new_status: str):
        """Change the status of a book."""
        if new_status not in BookStatus._value2member_map_:
            print("Error: Invalid status. Must be 'in_stock' or 'handed_out'.")
            return

        book_to_update = next((book for book in self.books if book.id == book_id), None)
        if book_to_update:
            book_to_update.status = BookStatus(new_status)
            self.save_books()
        else:
            print(f"Error: Book with ID {book_id} not found.")
