from flask import Flask, jsonify, render_template
import sys
from src import app
# ...
# @app.route('/')
# def index():
#     return render_template("index.html")
# @app.route('/article/<id>')
# def article(id):
#     return render_template("index.html")
if __name__ == '__main__':
    app.debug=True
    app.run(host=sys.argv[1], port=sys.argv[2])