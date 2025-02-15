from flask import Flask
import utils
app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'


