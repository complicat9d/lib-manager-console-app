from enum import Enum


class BookStatus(str, Enum):
    """Enumeration for book statuses."""

    IN_STOCK = "in_stock"
    HANDED_OUT = "handed_out"


class Book:
    """Class that represents a book's schema."""

    def __init__(
        self,
        book_id: int,
        title: str,
        author: str,
        year: int,
        status: BookStatus = BookStatus.IN_STOCK,
    ):
        """Initialize a book object with its attributes."""
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __repr__(self) -> str:
        """Return a string representation of the book."""
        return f"Book(ID: {self.id}, Title: '{self.title}', Author: '{self.author}', Year: {self.year}, Status: {self.status})"
