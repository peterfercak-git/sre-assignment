"""
Recruitment assignment for Site Reliability Engineers
"""
import requests
from PyPDF2 import PdfReader
from flask import Flask, abort

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
# Homepage endpoint
def index():
    return "Welcome!!"


@app.errorhandler(400)
def invalid_route(e):
    return "The value needs to be of a type integer, not string.", 400


@app.route('/<number>')
# Mime type endpoint
def mime_type(number):
    if number.isnumeric():
        r = requests.get("http://172.28.102.2:30001")
        if r.headers['Content-Type'] == "application/pdf":
            with open("my_pdf.pdf", 'wb') as my_data:
                my_data.write(r.content)

            with open("my_pdf.pdf", 'rb') as f:
                try:
                    pdf = PdfReader(f)
                    return f"Content-type: {r.headers['Content-Type']} (Not corrupted)\n{pdf.metadata}"
                except:
                    return f"Content-type: {r.headers['Content-Type']} (Corrupted)\n{pdf.metadata}"
        return f"Content-type {r.headers['Content-Type']}"
    abort(400)


@app.route('/health')
def health():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
