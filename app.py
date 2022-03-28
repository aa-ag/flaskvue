############------------ IMPORTS ------------############
from flask import Flask, jsonify
from flask_cors import CORS


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
        'title': 'Narrative Economics',
        'author': 'Robert Schiller',
        'read': True
    },
    {
        'title': 'A Dog\'s Tale',
        'author': 'Mark Twain',
        'read': True
    },
    {
        'title': 'Fooled by Randomness',
        'author': 'Nassim Taleb',
        'read': True
    }
]

############------------ FUNCTION(S) ------------############
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify('world, bb!')


############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app.run()