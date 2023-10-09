from utils import database, database2, database3

USER_CHOICE = """"
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit


Your choice: """

def menu():
    database3.create_book_file()
    user_input = input(USER_CHOICE)

    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            get_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print('Invalid input....try again.')
        user_input = input(USER_CHOICE)

def prompt_add_book():
    name = input("Enter the name of the book: ")
    author = input("Enter the author of the book: ")
    database3.add_book(name, author)

def get_books():
    books = database3.list_books()

    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, Read: {read}")

def prompt_read_book():
    name = input("Enter the name of the book you read: ")
    database3.mark_book_read(name)

def prompt_delete_book():
    name = input("Enter the name of the book you want to delete: ")
    database3.delete_book(name)

menu()