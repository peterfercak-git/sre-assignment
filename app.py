"""
Recruitment assignment for Site Reliability Engineers
"""
from requests import request
from flask import Flask, redirect, url_for, abort

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
# Homepage endpoint
def index():
    r = request(
        "GET",
        "127.0.0.1:3000",
        headers={},
        data={}
    )
    return f"You are on homepage - status code - {r.status_code}"


@app.errorhandler(404)
def invalid_route(e):
    return "The value needs to be of a type integer, not string.", 404


@app.route('/<number>')
# Mime type endpoint
def mime_type(number):
    if number.isnumeric():
        return "This is not expected response - dummy app has not been requested."
    abort(404)


@app.route('/health')
def health():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
