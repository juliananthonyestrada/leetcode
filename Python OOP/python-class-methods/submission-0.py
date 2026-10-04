class Library:
    books_available = 100    # Total books in library

    @classmethod
    def lend_books(cls, books_lent: int) -> None:
        cls.books_available -= books_lent
    
    @classmethod
    def return_books(cls, books_turned_in: int):
        cls.books_available += books_turned_in



# Don't change the code below
print(f"Initial status: {Library.books_available} books available")
Library.lend_books(30)
print(f"After lending: {Library.books_available} books available")
Library.return_books(10)
print(f"After return: {Library.books_available} books available")
