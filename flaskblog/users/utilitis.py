import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from flask import current_app
from flaskblog import mail


def delete_previous_img(img_path):
    if 'default.jpg' not in img_path:
        os.remove(os.path.join(current_app.root_path, "static/profile_pics", img_path))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, "static/profile_pics", picture_fn)

    output_size = (125, 125)
    img = Image.open(form_picture)
    img.thumbnail(output_size)
    img.save(picture_path)

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message("Password Reset Request", sender="noreply@demo.com", recipients=[user.email])
    msg.body = f""" To reset your password, visit the following link:
        {url_for('users.reset_token', token=token, _external=True)} 
        If you did not make this request, then simply ignore this mail and no changes will be made!

        Flask-Chonicel Blog Admin
        Gooday...!
    """
    # mail.send(msg)
