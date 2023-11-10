from flask import Flask

app = Flask(__name__)
POSTS = []  # list for objects of type post
USERS = []  # list for objects of type user

from app import views
from app import models
