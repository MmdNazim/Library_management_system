from person import Person
from exceptions import LibraryError

class Member(Person):
    def __init__(self, member_id, name, age):
        super().__init__(name, age)
        self.member_id = member_id
        self.borrowed_books = []


    def borrow_book(self, book):
        self.borrowed_books.append(book)

    def return_book(self, book):
        if book not in self.borrowed_books:
            raise LibraryError("This member did not borrow this book")
        self.borrowed_books.remove(book)

    def display_info(self):   
        super().display_info()   #Override kra hoiche    #reuse Person's name + age lines  
        print(f"Member ID: {self.member_id}")
        print(f"Borrowed Books: {len(self.borrowed_books)}")