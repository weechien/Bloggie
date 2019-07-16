from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {'title': 'Bloggie',
     'author': 'Goh Wee Chien',
     'date': '16th July 2019',
     'content': 'Welcome to my blog.'},
    {'title': 'Joyful Platter',
     'author': 'Chng Yu Sing',
     'date': '15th July 2019',
     'content': 'Come and join Joyful Platters!'}
]

@app.route("/")
def index():
    return render_template('index.html', posts=posts)


if __name__ == "__main__":
    app.run(debug=True)