'''
Problem Statement

Design and implement a Library Management System using Object-Oriented Programming (OOP).

The system should manage books, members, and library operations such as borrowing and returning books. The objective is to practice real-world OOP concepts by modeling a library environment.

System Requirements
Book Management

Each book in the library should contain:

Book ID
Title
Author
Availability Status

The system should allow:

Adding new books
Viewing book details
Marking books as borrowed
Marking books as returned
Member Management

Each library member should contain:

Member ID
Member Name
List of Borrowed Books

The system should allow members to:

Borrow books
Return books
View borrowed books
Library Management

The library should:

Store all books
Store all members
Search books
Issue books
Accept returned books
Display available books'''
class Book:
    def __init__(self,book_id,title,author):
        self.book_id=book_id
        self.title=title
        self.author=author
        self.is_available=True
    def display_details(self):
        status="Available" if self.is_available else "Borrowed"
        print(f"ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nStatus: {status}")
class Member:
    def __init__(self,member_id,name):
        self.member_id=member_id
        self.name=name
        self.borrowed_books=[]
    def borrow_book(self,book):
        if book.is_available:
            book.is_available=False
            print(f"Success: {book.title} borrowed by {self.name}")
        else:
            print(f"Error: {book.title} is currently unavailable")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.is_available=True
            self.borrowed_books.remove(book)
            print(f"Success: '{book.title}' returned by {self.name}")
        else:
            print(f"Error: {self.name} did not borrow this book.")
    def view_borrowed_books(self):
        print(f"\nBooks borrowed by {self.name}: ")
        if not self.borrowed_books:
            print("No books currently borrowed.")
        for book in self.borrowed_books:
            print(f"-{book.title} by {book.author}")
class Library:
    def __init__(self):
        self.books={}
        self.members={}
    def add_book(self,book_id,title,author):
        if book_id in self.books:
            print("Book Id already exists.")
        else:
            self.books[book_id]=Book(book_id,title,author)
            print(f"Book '{title}' added successfully.")
    def add_member(self,member_id,name):
        if member_id in self.members:
            print("Memberr Id already exists.")
        else:
            self.members[member_id]=Member(member_id,name)
            print(f"Member '{name}' registered successfully.")
    def search_book(self,keyword):
        print(f"\nSearch results for '{keyword}':")
        found=False
        for book in self.books.values():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                book.display_details()
                found=True
        if not found:
            print("No matching books found.")
    def issue_book(self,member_id,book_id):
        if member_id not in self.members:
            print("Member not found.")
            return 
        if book_id not in self.books:
            print("Book not found.")
            return 
        member=self.members[member_id]
        book=self.books[book_id]
        member.borrow_book(book)
    def accept_return(self,member_id,book_id):
        if member_id not in self.members:
            print("Member not found.")
            return 
        if book_id not in self.books:
            print("Book not found.")
            return 
        member=self.members[member_id]
        book=self.books[book_id]
        member.return_book(book)
    def display_available_books(self):
        print("\nAvailable Books in library:")
        available_found=False
        for book in self.books.values():
            if book.is_available:
                book.display_details()
                available_found=True
        if not available_found:
            print("No books currently available.")
my_library = Library()

my_library.add_book("B001", "The Alchemist", "Paulo Coelho")
my_library.add_book("B002", "Atomic Habits", "James Clear")
my_library.add_book("B003", "Clean Code", "Robert C. Martin")

my_library.add_member("M001", "Archana")
my_library.add_member("M002", "Shreyas")

my_library.display_available_books()

print("\n--- Borrowing Operation ---")
my_library.issue_book("M001", "B001")  
my_library.members["M001"].view_borrowed_books()

my_library.display_available_books()

print("\n--- Return Operation ---")
my_library.accept_return("M001", "B001")

print("\n--- Search Operation ---")
my_library.search_book("Atomic")