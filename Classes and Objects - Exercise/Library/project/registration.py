from project import User
from project import Library

class Registration:

    def add_user(self, user: User, library: Library) -> str:
        if user not in library.user_records:
            library.user_records.append(user)

        return f"User with id = {user.user_id} already registered in the library!"

    def remove_user(self, user: User, library: Library) -> str:
        if user in library.user_records:
            library.user_records.remove(user)

        return "We could not find such user to remove!"

    def change_username(self, user_id: int, new_username: str, library: Library) -> str:
        try:
            user = next(filter(lambda u: u.user_id == user_id, library.user_records))
        except StopIteration:
            return f"There is no user with id = {user_id}!"

        if user.username == new_username:
            return f"Please check again the provided username - it should be different than the username used so far!"

        try:
            library.rented_books[new_username] = library.rented_books.pop(user.username)
        except KeyError:
            pass

        user.username = new_username
        return f"Username successfully changed to: {new_username} for user id: {user_id}"