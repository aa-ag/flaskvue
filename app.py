############------------ IMPORTS ------------############
from crypt import methods
from flask import Flask, jsonify
from flask_cors import CORS
from itsdangerous import json


############------------ GLOBAL VARIABLE(S) ------------############
# configuration
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


############------------ FUNCTION(S) ------------############
@app.route('/hello', methods=['GET'])
def hello_world():
    return jsonify('world')


############------------ DRIVER CODE ------------############
