class Book:
    """A simple Book class to demonstrate Python magic methods.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year.
    """

    def __init__(self, title: str, author: str, year: int):
        """Constructor: initialize title, author and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: runs when the object is about to be garbage collected.

        Note: timing of __del__ is implementation-dependent. In CPython, calling
        `del` on the last reference typically triggers it immediately.
        """
        print(f"Deleting {self.title}")

    def __str__(self) -> str:
        """Human-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Official representation — should be able to recreate the object.

        Using !r ensures proper quoting/escaping of the title and author.
        """
        return f"Book({self.title!r}, {self.author!r}, {self.year})"
