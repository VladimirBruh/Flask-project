import flask
from app import app, USERS, POSTS, models
from flask import request, Response
import json
from http import HTTPStatus

@app.route("/")
def index():
    return "<h1>Hello</h1>"


@app.post("/user/create")
def user_create():
    data = request.get_json()
    id = len(USERS)
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    posts = []
    # todo: check phone and email for validity
    if not models.User.is_valid_email(email):
        return Response(status=HTTPStatus.BAD_REQUEST)
    user = models.User(id, first_name, last_name, email, posts)
    user.is_valid_email(user.email)
    USERS.append(user)
    response = Response(
        json.dumps(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "total_reactions": user.total_reactions,
                "posts": user.posts,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="oplication/json",
    )
    return response


@app.get("/user/<int:user_id>")
def user_get(user_id):
    if isinstance(user_id, int) == False or user_id < 0 or user_id >= len(USERS):
        return Response(status=HTTPStatus.NO_CONTENT)
    user = USERS[user_id]
    response = Response(
        json.dumps(
            {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "total_reactions": user.total_reactions,
                "posts": user.posts,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="oplication/json",
    )
    return response


@app.post("/posts/create")
def create_post():
    data = request.get_json()
    id = len(POSTS)
    author_id = data["author_id"]
    text = data["text"]
    reactions = []

    post = models.Post(id,author_id,text,reactions)
    POSTS.append(post)
    response = Response(
        json.dumps(
            {
                "id": post.id,
                "author_id": post.author_id,
                "text": post.text,
                "reactions": post.reactions,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="oplication/json",
    )
    return response

@app.get("/posts/<int:post_id>")
def get_post(post_id):
    post = POSTS[post_id]
    response = Response(
        json.dumps(
            {
                "id": post.id,
                "author_id": post.author_id,
                "text": post.text,
                "reactions": post.reactions,
            }
        ),
        HTTPStatus.CREATED,
        mimetype="oplication/json",
    )
    return response
