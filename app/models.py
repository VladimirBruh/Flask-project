import re


class Post():
    def __init__(self,id,author_id,text,reactions):
        self.id=id
        self.author_id = author_id
        self.text = text
        self.reactions = reactions
class User():
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
    def append_post(self,post):
        ...


posts = [
    {
        "id": "0",
        "auhor_id": "1",
        "text": "hello",
        "reactions": ["hello","nice"]
    },
    {
        "id": "1",
        "auhor_id": "1",
        "text": "hello",
        "reactions": ["hello1","nice1","niiice"]
    },
]

posts.sort(key=lambda x:x["reactions"],reverse=False)
print(posts)