import flask
from app import app, USERS, POSTS, models
from flask import request, Response
import json
from http import HTTPStatus

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

    user = USERS[int(author_id)]
    user.posts.append(id)

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

@app.post("/posts/<int:post_id>/reaction")
def post_reaction(post_id):
        data = request.get_json()

        post = POSTS[post_id]
        post.reactions.append(data["reaction"])

        user_id = int(data["user_id"])
        user = USERS[user_id]
        user.total_reactions+=1
        return flask.jsonify({'status':'200'}), 200



@app.get("/users/<int:user_id>/posts")
def get_posts(user_id):
    data = request.get_json()
    user = USERS[user_id]
    posts_id = user.posts # хуйня с числами, а нужно по этим числам найти посты
    posts_class = []
    posts = []
    for i in posts_id:
        posts_class.append(POSTS[i])
    for i in posts_class:
        posts.append(
            {
            "id": i.id,
            "auhor_id": i.author_id,
            "text": i.text,
            "reactions": i.reactions
            }
        )
    if data["sort"]=="asc":
        posts.sort(key=lambda x:x["reactions"],reverse=False)
    elif data["sort"]=="desc":
        posts.sort(key=lambda x: x["reactions"], reverse=True)
    else:
        return flask.jsonify({'error':'not found'}), 404
    return posts