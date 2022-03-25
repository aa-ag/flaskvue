############------------ IMPORTS ------------############
from flask import Flask, jsonify
from flask_cors import CORS


############------------ GLOBAL VARIABLE(S) ------------############
# configuration
DEBUG = True

# instantiate app
app = Flask(__name__)
app.config.from_object(__name__)

############------------ FUNCTION(S) ------------############


############------------ DRIVER CODE ------------############
