import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:////' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    subtitle = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('index.html', now = datetime.utcnow(), posts = posts)

@app.route('/about')
def about():
    return render_template('about.html', now=datetime.utcnow())

@app.route('/show/<int:post_id>')
def show(post_id):
    post = BlogPost.query.filter_by(id = post_id).one()
    return render_template('show.html', now = datetime.utcnow(), post = post)

@app.route('/new')
def new():
    return render_template('new.html', now=datetime.utcnow())

@app.route('/create', methods=['POST'])
def create():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author =  request.form['author']
    content = request.form['content']
    # return '<h1>Title: {}, Subtitle: {}, Author: {}, Content: {} </h1>'.format(title, subtitle, author, content)
    post = BlogPost(title = title, subtitle = subtitle, author = author, content = content, date_posted = datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/hello')
def hello():
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run(debug=True)
