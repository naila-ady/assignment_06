"""Create a class Book with a class variable total_books. Add a class method increment_book_count()
to increase the count when a new book is added.

"""
class Book:
    total_books = 0
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
        
    def __init__(self, title):
        self.title = title  # Instance variable to store the book's title
        Book.increment_book_count()  # Increment the book count whenever a new book is created

book1=Book("THE KING OF LEGENDS")
book2=Book("The Great GatsBy")

print(f"Th total number of books {Book.total_books}")
    