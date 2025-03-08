# Custom Exception Classes
class BookNotFoundException(Exception):
    """Raised when a book doesn't exist in the library"""
    pass

class BookAlreadyBorrowedException(Exception):
    """Raised when attempting to borrow an already borrowed book"""
    pass

class MemberLimitExceededException(Exception):
    """Raised when a member exceeds their borrowing limit"""
    pass

# Book Class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"

# Member Class
class Member:
    MAX_BOOKS = 3
    
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if len(self.borrowed_books) >= self.MAX_BOOKS:
            raise MemberLimitExceededException(
                f"{self.name} has reached the maximum limit of {self.MAX_BOOKS} books"
            )
        if book.is_borrowed:
            raise BookAlreadyBorrowedException(
                f"'{book.title}' is already borrowed"
            )
        book.is_borrowed = True
        self.borrowed_books.append(book)
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            return True
        return False
    
    def __str__(self):
        return f"{self.name} - Borrowed books: {len(self.borrowed_books)}"

# Library Class
class Library:
    def __init__(self):
        self.books = []
        self.members = []
    
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
        return book
    
    def add_member(self, name):
        member = Member(name)
        self.members.append(member)
        return member
    
    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        raise BookNotFoundException(f"Book '{title}' not found in library")
    
    def find_member(self, name):
        for member in self.members:
            if member.name.lower() == name.lower():
                return member
        return None
    
    def borrow_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise Exception(f"Member '{member_name}' not found")
        book = self.find_book(book_title)
        member.borrow_book(book)
    
    def return_book(self, member_name, book_title):
        member = self.find_member(member_name)
        if not member:
            raise Exception(f"Member '{member_name}' not found")
        book = self.find_book(book_title)
        if not member.return_book(book):
            raise Exception(f"'{book_title}' was not borrowed by {member_name}")

# Test the Library System
def test_library_system():
    # Create library instance
    library = Library()
    
    try:
        # Test 1: Adding books and members
        print("Test 1: Adding books and members")
        book1 = library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
        book2 = library.add_book("1984", "George Orwell")
        book3 = library.add_book("To Kill a Mockingbird", "Harper Lee")
        book4 = library.add_book("Pride and Prejudice", "Jane Austen")
        
        member1 = library.add_member("Alice")
        member2 = library.add_member("Bob")
        
        print(f"Added books: {len(library.books)}")
        print(f"Added members: {len(library.members)}")
        print()

        # Test 2: Borrowing books
        print("Test 2: Borrowing books")
        library.borrow_book("Alice", "The Great Gatsby")
        library.borrow_book("Alice", "1984")
        print(f"{member1}")
        print(book1)
        print(book2)
        print()

        # Test 3: BookNotFoundException
        print("Test 3: Trying to borrow non-existent book")
        try:
            library.borrow_book("Bob", "Non-existent Book")
        except BookNotFoundException as e:
            print(f"Exception caught: {e}")
        print()

        # Test 4: BookAlreadyBorrowedException
        print("Test 4: Trying to borrow already borrowed book")
        try:
            library.borrow_book("Bob", "The Great Gatsby")
        except BookAlreadyBorrowedException as e:
            print(f"Exception caught: {e}")
        print()

        # Test 5: MemberLimitExceededException
        print("Test 5: Trying to exceed borrowing limit")
        try:
            library.borrow_book("Alice", "To Kill a Mockingbird")
            library.borrow_book("Alice", "Pride and Prejudice")
        except MemberLimitExceededException as e:
            print(f"Exception caught: {e}")
        print()

        # Test 6: Returning books
        print("Test 6: Returning books")
        library.return_book("Alice", "The Great Gatsby")
        print(f"After return: {member1}")
        print(book1)

    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    test_library_system()