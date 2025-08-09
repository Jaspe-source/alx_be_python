class Book:
    """A simple Book class to demonstrate Python magic methods."""

    def __init__(self, title, author, year):
        """Constructor: initialize title, author and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Destructor: runs when the object is about to be garbage collected."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Human-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official representation — should be able to recreate the object."""
        return f"Book('{self.title}', '{self.author}', {self.year})"
