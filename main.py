"""#[NOTE:]
while True: is used to create an intentional infinite loop that runs continuously until a specific condition inside the loop stops

"break" terminates the current loop.
"return" exits the current function entirely.

Remember this distinction:
- raise is used to send an exception when something goes wrong.
- except is used to catch and handle that exception.
"""

from person import Person
from member import Member
from book import Book
from library import Library
from exceptions import LibraryError


def display_menu():
    line = "=" * 40
    print(line)
    print(Library.get_system_name())
    print(line)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Show All Members")
    print("7. Search Book")
    print("8. Exit")


def read_choice():
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice! Please enter a number 1 to 8.")
        return None
    if choice<1 or choice>8:
        print("Invalid choice! Please enter a number 1 to 8.")
        return None
    return choice


def read_age():
     text = input("Enter your age: ").strip()
     if text == "":
         raise ValueError("Age cannot be empty")
     try:
         return int(text)
     except ValueError:
         print("Age must be a number")


def add_book_ui(library):
    print("------ Add New Book ------")
    title = input("Enter book title: ")
    author = input("Enter author: ")
    isbn = input("Enter ISBN: ")
    library.add_book(Book(title, author, isbn))


def register_member_ui(library):
    print("------ Register Member ------")
    member_id = input("Enter member ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    library.register_member(Member(member_id, name, age))


def borrow_book_ui(library):
    print("------ Borrow Book ------")
    member_id = input("Enter member ID: ")
    isbn = input("Enter ISBN: ")
    library.borrow_book(member_id, isbn)


def return_book_ui(library):
    print("------ Return Book ------")
    member_id = input("Enter member ID: ")
    isbn = input("Enter ISBN: ")
    library.return_book(member_id, isbn)


def search_book_ui(library):
    print("------ Search Book ------")
    title = input("Enter book title: ")
    library.search_book(title)



def main():
    library = Library()

    actions = {
        1 : add_book_ui,
        2 : register_member_ui,
        3 : borrow_book_ui,
        4 : return_book_ui,
        5 : lambda lib: lib.show_books(),
        6 : lambda lib: lib.show_members(),
        7 : search_book_ui 
    }

    while True:
        try:
            display_menu()
            choice = read_choice()

            if choice is None:
                pass       # message already shown by "read_choice()"
            elif choice == 8:
                print("Thank you for using Library Management System.")
                print("Goodbye!")
                break
            else:
                try:
                    actions[choice](library)
                except LibraryError as error:     # rule broken (duplicate, not found...) || LibraryError = Business rule violations, such as book not found or duplicate ISBN
                    print(error)
                except ValueError as error:     # bad input (empty, bad age...) || ValueError = Invalid input, such as an invalid age or data value
                    print(f"Error: {error}")
                except Exception as error:     # anything unexpected || Exception = Unexpected errors
                    print(f"Unexpected error: {error}")


            input("Press Enter to continue...")
            print()

        except(KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break
main()