from project import Movie
from project import User


class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def _find_user_by_username(self, username):
        user = [u for u in self.users_collection if u.username == username]
        return user[0] if user else None

    def register_user(self, username: str, age: int):
        if self._find_user_by_username(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)

        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        if not user:
            raise Exception("This user does not exist!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attr, new_value in kwargs.items():
            setattr(movie, attr, new_value)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        user.movies_owned.remove(movie)
        self.movies_collection.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user.movies_liked.append(movie)
        movie.likes += 1

        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user.movies_liked.remove(movie)
        movie.likes -= 1

        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'
