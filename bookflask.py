from database import db_session, init_db
from models import Book, BookJSONEnconder
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS, cross_origin

init_db()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy dog'
app.config['CORS_HEADERS'] = 'Content-Type'

cors = CORS(app, resources={r"/books": {"origins": "localhost"}})

app.json_encoder = BookJSONEnconder

@app.route('/')
def hello_world():
    return render_template("booklist.html")
    # return 'Hello, World!'

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('static/js', path)

@app.route('/books/list')
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def list_books():
    return jsonify(Book.query.all())

@app.route('/books/edit', methods=['POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def edit_book():
    print request.form
    try:
        BookToEdit = Book.query.filter(Book.id == request.form['DT_RowId']).first()
        BookToEdit.status = request.form['status']
        db_session.commit()
    except:
        return abort(500)
    return "ok"

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
