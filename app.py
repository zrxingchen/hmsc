from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello 地狱 </h1>'