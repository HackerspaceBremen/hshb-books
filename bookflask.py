from database import db_session, init_db
from models import Book
from flask import Flask, request

init_db()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/books/')
def list_books():
    return str(Book.query.all())

@app.route('/books/add', methods=['POST', 'GET'])
def add_book():
    if request.method == 'POST':
        try:
            title = request.form['title']
        except:
            title = None
        try:
            author = request.form['author']
        except:
            author = None
        try:
            isbn = request.form['isbn']
        except:
            isbn = None
        try:
            status = request.form['status']
        except:
            status = None
    elif request.method == 'GET':
        try:
            title = request.args.get('title',None)
        except:
            title = None
        try:
            author = request.args.get('author',None)
        except:
            author = None
        try:
            isbn = request.args.get('isbn',None)
        except:
            isbn = None
        try:
            status = request.args.get('status',None)
        except:
            status = None
    else:
        title = None
        author = None
        isbn = None
        status = None

    b = Book(title, author, isbn, status)
    if not title == None:
        try:
            db_session.add(b)
            db_session.commit()
            result = 'success' + str(b)
        except:
            result = 'failed'
    else:
        result = 'no title'

    return result

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()
