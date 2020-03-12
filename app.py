from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', now=datetime.utcnow())

@app.route('/about')
def about():
    return render_template('about.html', now=datetime.utcnow())

@app.route('/post')
def post():
    return render_template('post.html', now=datetime.utcnow())

@app.route('/hello')
def hello():
    return 'Hello, World!'
 
if __name__ == '__main__':
    app.run(debug=True)
