# 11. Class Methods
# Assignment:
# Create a class Book with a class variable total_books.
# Add a class method increment_book_count() to increase the count when a new book is added.

class Book:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.increment_book_count()

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        return f"Total books: {cls.total_books}"

# Creating instances of Book
book1: Book = Book("1984", "George Orwell")
book2: Book = Book("To Kill a Mockingbird", "Harper Lee")

# Printing the total book count
print(book1.increment_book_count())
print(book2.increment_book_count())
