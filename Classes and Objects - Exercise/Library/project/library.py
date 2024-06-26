from project import User


class Library:

    def __init__(self):
        self.user_records = []
        self.books_available = {}   # {author: [book available, book..]}
        self.rented_books = {}      # {username: {book_names: days_to_return}}

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author]:
            self.books_available[author].remove(book_name)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name: days_to_return}

            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for info in self.rented_books.values():
            if book_name in info:
                return f'The book "{book_name}" is already rented and will be available in {info[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> str:
        if book_name in self.rented_books[user.username]:
            del self.rented_books[user.username][book_name]
            user.books.remove(book_name)
            self.books_available[author].append(book_name)

        return f"{user.username} doesn't have this book in his/her records!"
