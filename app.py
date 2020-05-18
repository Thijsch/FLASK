from flask import Flask, render_template, request

# Constructor
app = Flask(__name__)


# URL
@app.route('/')
def hello_world():
    naam = request.args.get("naam", "")
    achternaam = request.args.get("achternaam", "")
    return render_template("Hello World.html", naam=naam,
                           achternaam=achternaam)


# @approute('/show_color')
# def show_color():
#     kleur = request.args.get("kleur", "white")
#     return render_template("kleur.html", kleur=kleur)


if __name__ == '__main__':
    app.run()
