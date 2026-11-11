class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.__available = True


    @property
    def available(self):
        return self.__available 

    #[NOTE: "isinstance()" is a built-in Python function that helps you check the data type of a value or object.]
    #[NOTE: if not condition: means execute this block when the condition is NOT true.]
    @available.setter
    def available(self, value):
        if not isinstance(value, bool):
            #[NOTE:We use "raise" because we want to stop the operation and report an error when the user provides an invalid value. Think of raise as saying: "Something is wrong. Don't continue this operation."]
            raise ValueError("available must be True or False.")
        self.__available = value



    

    def display_book(self):
        # status = "Available" if self.available else "Borrowed"  #[NOTE: This called: "Ternary Conditional Expression"]
        if self.available:
            status = "Available"

        else:
            status = "Borrowed"

        print(f"ISBN : {self.isbn}")
        print(f"Title : {self.title}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")