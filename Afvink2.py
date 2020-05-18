from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/index', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        seq = request.form.get("seq", "")
        return render_template("Gene_check.htm", seq=seq)
    else:
        return render_template("Gene_check.htm", seq="Niks gevonden")


    # DNAseq = request.args.get("naam", "")
    # achternaam = request.args.get("achternaam", "")
    # return render_template("Hello World.html", naam=naam,
    #                        achternaam=achternaam)


if __name__ == '__main__':
    app.run()
