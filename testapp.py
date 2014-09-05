# coding:utf-8
#!/usr/bin/python3

from flask import Flask, render_template, url_for,\
        request, redirect, g

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/foo')
def foo():
    return "Foo Foo"

@app.route('/post/<words>')
def show_post(words=None):

    return render_template('post.html', words=words)

if __name__ == '__main__':
    app.debug = True
    app.run()