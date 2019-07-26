import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from application import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static', 'profile_pics', picture_fn)
    output_size = (125, 125)
    with Image.open(form_picture) as img:
        img.thumbnail(output_size)
        img.save(picture_path)

    return picture_fn


def remove_picture(picture):
    if picture == 'default.jpg':
        return
    picture_path = os.path.join(
        current_app.root_path, 'static', 'profile_pics', picture)
    os.remove(picture_path)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender=os.environ.get('EMAIL_USER'),
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
