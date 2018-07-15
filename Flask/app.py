#!/usr/bin/env python
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
      return render_template("views/index.html")
@app.route('/<int:id>')
def number(id):
      return '<h1>You Entered: {0}<h1/>'.format(id)
if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080, debug=True)
