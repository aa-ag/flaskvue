############------------ IMPORTS ------------############
from crypt import methods
from os import remove
from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

############------------ GLOBAL VARIABLE(S) ------------############
# configuration
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# dummy data to start
BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Narrative Economics',
        'author': 'Robert Schiller',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'A Dog\'s Tale',
        'author': 'Mark Twain',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Fooled by Randomness',
        'author': 'Nassim Taleb',
        'read': True
    }
]

############------------ FUNCTION(S) ------------############
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify('world, bb!')


@app.route('/books', methods=['GET', 'POST'])
def list_all_books():
    response_object = {'status': 'success'}

    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append(
            {   
                'id': uuid.uuid4().hex,
                'title': post_data.get('title'),
                'author': post_data.get('author'),
                'read': post_data.get('read'),
            }
        )
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    
    response_object = {'status': 'success'}

    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        
        response_object['message'] = 'Book updated!'
    
    if request.method == 'DELETE':
        remove_book(book_id)
        
        response_object['message'] = 'Book removed!'

    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False
    
############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()