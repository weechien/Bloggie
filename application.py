from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '36dfdfb7754d4c9876f98f83b59f9200'

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
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))

    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check username and password.', 'danger'
            )
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
