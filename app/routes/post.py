from flask import Blueprint
from ..extensions import db
from ..models.post import Post

post = Blueprint('post',__name__)

@post.route("/post/<subject>")
def create_user(subject):
    post = Post(subject=subject)
    db.session.add(post)
    db.session.commit()
    return 'Тема успешно создана!'