from flask import Flask, redirect

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/<int:int_id>', methods=['GET'])
def show_post(int_id):
    if type(int_id) is int:
        # return "Correct"
        return "This is not expected response - dummy app has not been requested."
    return redirect('/error')


@app.route('/error', methods=['GET'])
def incorrect_param():
    return "Incorrect type of parameter"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
