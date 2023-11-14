import re


class Post:
    def __init__(self, id, author_id, text, reactions):
        self.id = id
        self.author_id = author_id
        self.text = text
        self.reactions = reactions


class User:
    def __init__(self, id, first_name, last_name, email, posts, total_reactions=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.total_reactions = total_reactions
        self.posts = posts

    @staticmethod
    def is_valid_email(email):
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return True
        return False

    def __lt__(self, other):  # для функции sorted(USERS)
        return self.total_reactions < other.total_reactions
