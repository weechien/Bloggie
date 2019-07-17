from flask import Flask, render_template, url_for
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

@app.route('/register')
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
