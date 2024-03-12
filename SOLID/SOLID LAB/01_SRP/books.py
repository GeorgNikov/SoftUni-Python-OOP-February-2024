class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

    def __str__(self):
        return f"Title {self.title} from {self.author}"


class Library:

    def __init__(self, books):
        self.books = books

    def add_book(self, book):
        if book in self.books:
            return f'{book.title} is already in the Library!'
        self.books.append(book)

    def remove_book(self, title):
        book = self.find_book(title)

        if not book:
            return f"{title} not in library"

        self.books.remove(book[0])
        return f"{title} was removed from Library!"

    def find_book(self, title):
        books = [b for b in self.books if b.title == title]

        if not books:
            raise ValueError("Title not found")

        return books


book1 = Book('Programming with Python', 'Svetlin Nakov')
book2 = Book('Programming with C#', 'Svetlin Nakov')
book2.turn_page(350)
print(book1)
print(book2)
books = [book1, book2]
library = Library(books)
# library.add_book(book1)
# library.add_book(book2)
library.remove_book('Programming with C#')
print(library.find_book('Programming with Python'))
print(library.find_book('Programming with C#'))

# NOT WORKING