#!/usr/bin/env python3
"""Written in python 3."""
#
# Article reporting tool

from flask import Flask, request, redirect, url_for

from forumdb import get_posts, add_post

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():


@app.route('/', methods=['POST'])
def post():


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
