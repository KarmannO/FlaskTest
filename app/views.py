from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    user = {'nickname': 'Dimas'}
    return render_template('index.html', title='Home', posts=posts, user=user)