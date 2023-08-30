class Book:
    id_counter = 0

    def __init__(self, title, author, level):
        Book.id_counter += 1
        self.book_id = Book.id_counter
        self.title = title
        self.author = author
        self.level = level
        self.is_available = True


class Member:
    id_counter = 0

    def __init__(self, name, email, level):
        Member.id_counter += 1
        self.member_id = Member.id_counter
        self.name = name
        self.email = email
        self.level = level
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available and self.level == book.level:
            self.borrowed_books.append(book)
            book.is_available = False
            return True
        else:
            return False

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        else:
            return False


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def add_member(self, member):
        self.members.append(member)

    def display_books(self):
        for book in self.books:
            print(f"Book ID: {book.book_id}, Title: {book.title}, Author: {book.author}, Level: {book.level}, Availability: {'Available' if book.is_available else 'Not Available'}")

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def display_members(self):
        for member in self.members:
            print(f"Member ID: {member.member_id}, Name: {member.name}, Email: {member.email}, Level: {member.level}")

    def find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member


library = Library()
print(' Welcome to the Library System '.center(100,'-'))
while True:
    print("1. Add Member")
    print("2. Edit Member")
    print("3. Show Members")
    print("4. Delete Member")
    print("5. Add Book")
    print("6. Show Books")
    print("7. Borrow Book")
    print("8. Return Book")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter Member Name: ")
        email = input("Enter Member Email: ")
        level = input("Enter Member Level: ")
        member = Member(name, email, level)
        library.add_member(member)
        print("Member added successfully.")

    elif choice == '2':
        # TODO: Implement Edit Member option
        pass

    elif choice == '3':
        library.display_members()

    elif choice == '4':
        # TODO: Implement Delete Member option
        pass

    elif choice == '5':
        title = input("Enter Book Title: ")
        author = input("Enter Book Author: ")
        level = input("Enter Book Level: ")
        book = Book(title, author, level)
        library.add_book(book)
        print("Book added successfully.")

    elif choice == '6':
        library.display_books()

    elif choice == '7':
        # TODO: Implement Borrow Book option
        pass

    elif choice == '8':
        # TODO: Implement Return Book option
        pass

    elif choice == '9':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")
