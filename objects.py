from reader import Reader
from book import Book

user = Reader("Ivan Nechaev", "26.10.2001", 88006105521)

while True:
    command = input("input command ")
    if command == "rent":
        title = input()
        author = input()
        pages = input()
        user.rent_book(Book(title, author, pages))
        print(user)

    if command == "return":
        title = input()
        author = input()
        pages = input()
        user.return_book(title, author, pages)
        print(user)

    if command == "return author":
        author = input("input author ")
        user.return_author(author)
        print(user)

    if command == "stop":
        break
