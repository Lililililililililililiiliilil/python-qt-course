from book import Book


class Reader:
    def __init__(self, name, birthday, mobile):
        self.name = name
        self.birthday = birthday
        self.mobile = mobile
        self.book_list = list()

    def __str__(self):
        return f"{self.name}, {self.birthday}, {self.mobile}, {self.print_books()}"

    def rent_book(self, book):
        if book not in self.book_list:
            self.book_list.append(book)
        else:
            return "The book is already taken!"

    def return_book(self, title, author, pages):
        try:
            self.book_list.remove(Book(title, author, pages))
        except ValueError:
            print("There is no such book!")

    def set_name(self, name):
        self.name = name

    def set_mobile(self, mobile):
        self.mobile = mobile

    def set_book_list(self, books):
        self.book_list = books

    def get_name(self):
        return self.name

    def get_birthday(self):
        return self.birthday

    def get_mobile(self):
        return self.mobile

    def get_book_list(self):
        return self.book_list

    def print_books(self):
        str = ""
        for book in self.book_list:
            str += book.get_author() + " - " + book.get_title() + ", "
        return str

    def return_author(self, author):
        for book in self.book_list:
            print(book.get_author(), author)
            if book.get_author() == author:
                self.book_list.remove(book)
