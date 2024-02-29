import re


class Profile:

    def __init__(self, username: str, password: str):
        if not 5 <= len(username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")

        if len(password) < 8 or not re.search(r"\d+", password) or not re.search(r"[A-Z]+", password):
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")

        self.__username = username
        self.__password = password

    def __str__(self):
        return f'You have a profile with username: "{self.__username}" and password: {"*" * len(self.__password)}'


correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
