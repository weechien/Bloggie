from flask import render_template, url_for, flash, redirect, request
from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from application.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {'title': 'Bloggie',
     'author': 'Goh Wee Chien',
     'date': '16th July 2019',
     'content': 'Welcome to my blog.'},
    {'title': 'Joyful Platter',
     'author': 'Chng Yu Sing',
     'date': '15th July 2019',
     'content': 'Come and join Joyful Platters!'},
    {'title': 'Joyful Platter',
     'author': 'Chng Yu Sing',
     'date': '15th July 2019',
     'content': 'Come and join Joyful Platters!'},
    {'title': 'Joyful Platter',
     'author': 'Chng Yu Sing',
     'date': '15th July 2019',
     'content': 'Come and join Joyful Platters!'},
    {'title': 'Joyful Platter',
     'author': 'Chng Yu Sing',
     'date': '15th July 2019',
     'content': 'Come and join Joyful Platters!'},
]


@app.route('/')
def index():
    return render_template('index.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You account has been created! You are now able to log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')