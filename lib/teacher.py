from user import User
import random

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        # Call the __init__ method of the parent class (User)
        super().__init__(first_name, last_name)

    def teach(self):
        # Return a random element from the knowledge list
        return random.choice(self.knowledge)
