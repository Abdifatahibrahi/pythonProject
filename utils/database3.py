from typing import List, Dict, Union
from .database_connection import  DatabaseConnection

books_file = 'books.json'
Book = List[Dict]
def create_book_file() -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")



def add_book(name:str, author:str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO books VALUES(?, ?, False)", (name, author))


def list_books() -> Book:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * from books")
        books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books



def mark_book_read(name: str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"update books set read='True' where name == ?", (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection() as connection:
        cursor = connection.cursor()
        cursor.execute("Delete from books where name==?", (name,))


