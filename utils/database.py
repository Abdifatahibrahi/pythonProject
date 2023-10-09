

books_file = 'books.txt'

def create_book_file():
    with open(books_file, 'w'):
        pass
def add_book(name, author):
    with open(books_file, 'a') as b:
        b.write(f"{name}, {author}, {False}\n")


def list_books():
    with open(books_file, 'r') as file:
        lines = [book.strip().split(',') for book in file.readlines()]

        return [
            {'name': line[0], 'author': line[1], 'read': line[2]} for line in lines
        ]


def mark_book_read(name):
    books = list_books()
    # print(books)
    for book in books:
        if book['name'] == name:
            book['read'] = True
        _save_all_books(books)
def _save_all_books(books):
    with open(books_file, "w") as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")
def delete_book(name):
    books = list_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

