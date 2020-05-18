from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/show_color', methods=["POST", "GET"])
def hello_world():
    return hello_world


if __name__ == '__main__':
    app.run()
