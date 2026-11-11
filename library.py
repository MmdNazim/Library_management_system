"""
#[NOTE: Composition is an object-oriented programming concept where one class contains objects of other classes as its attributes.]
#[NOTE: Remember: Inheritance represents an is-a relationship. Composition represents a has-a relationship.]
#[NOTE: A Class Method is a method that belongs to a class rather than an individual object.]

#Normal method
self = Individual object
Works with individual object's information.
Example: Book title, member name, library name.

#Class method
cls = Class itself
Works with information or behaviour associated with the class.
Example: System name, class-level settings, alternative constructors.]
"""
from exceptions import LibraryError

class Library:
    system_name = "LIBRARY MANAGEMENT SYSTEM"

    @classmethod                # class method
    def get_system_name(cls):   # cls refers to the class itself.
        return cls.system_name  # Accesses the class variable.


    def __init__(self):
        self.books = []
        self.members = []


    #_________Create small private helper functions:___________
    #_____"This is an internal/helper method. I mainly "(_)" intend to use it inside this class."_______
    def _find_book(self, isbn):
        for book in self.books:
            if book.isbn.lower() == isbn.strip().lower():
                return book
        return None

    def _find_member(self, member_id):
        for member in self.members:
            if member.member_id.lower() == member_id.strip().lower():
                return member
        return None


    def add_book(self, book):
        if self._find_book(book.isbn):
            raise LibraryError("Error: ISBN already exists.")
        self.books.append(book)
        print("Book added successfully")


    def register_member(self, member):
        if self._find_member(member.member_id):
            raise LibraryError("Error: Member ID already exists")
        self.members.append(member)
        print("Member registered successfully")

    def borrow_book(self, member_id, isbn):
        member = self._find_member(member_id)
        if member is None:
            raise LibraryError("Member not found")
        book = self._find_book(isbn)
        if book is None:
            raise LibraryError("Book not found")
        member.borrow_book(book)
        print("Book borrowed successfully")
        

    def return_book(self, member_id, isbn):
        member = self._find_member(member_id)
        if member is None:
            raise LibraryError("Member not found")
        book = self._find_book(isbn)
        if book is None:
            raise LibraryError("Book not found")
        member.return_book(book)
        print("Book returned successfully")



    def show_books(self):
        print("-----------------BooK List-----------------")
        if not self.books:
            print("No books in the library yet")
            return
        for book in self.books:
            book.display_book()
            print("_" * 40)

    def show_members(self):
            print("---------------Member List---------------")
            if not self.members:
                print("No member registered yet")
                return
            for member in self.members:
                member.display_info()
                print("_" * 40)

    def search_book(self, title):
        if title.strip() == "":
            raise ValueError("Book title cannot be empty") 
        #matches = [book for book in self.books if title.strip().lower() in book.title.lower()]   [NOTE: "matches to append" this lines are same and we represent it this way also]
        matches = []
        for book in self.books:
            if title.strip().lower() in book.title.lower():
                matches.append(book)
        if not matches:
            raise LibraryError("Book not found")
        print("Book found")
        for book in matches:
            book.display_book()
            print()     #[NOTE: print() is used to create an empty line (blank line) between two book records.]