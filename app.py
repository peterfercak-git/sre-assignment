"""
Recruitment assignment for Site Reliability Engineers
"""

from flask import Flask, redirect, url_for

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
# Homepage endpoint
def index():
    return "You are on homepage."


@app.route('/error')
# Error endpoint
def error():
    return "Incorrect type of parameter"


@app.route('/<number>')
# Mime type endpoint
def mime_type(number):
    if number.isnumeric():
        return "This is not expected response - dummy app has not been requested."
    return redirect(url_for('error'))


@app.route('/health')
def health():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
