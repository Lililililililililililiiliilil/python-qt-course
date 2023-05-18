import this


class Book:
    def __init__(self, title, author, pages):
        self.__title = title
        self.__author = author
        self.__pages = pages

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_pages(self):
        return self.__pages

    def __str__(self):
        return "Author: " + self.__author + ", title: " + self.__title + ", pages: " + str(self.__pages)

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.__author == other.__author) and (self.__title == other.__author) and (
                self.__pages == other.__pages)
