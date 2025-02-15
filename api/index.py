from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return 'hi'


