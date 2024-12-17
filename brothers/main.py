
from flask import Flask , render_template


app=Flask(__name__)


@app.route("/")
def main():
    return render_template("welcome_page.html")


@app.route("/php")
def php():
    return render_template("2.php")


if __name__=="__main__":
    app.run(debug=True,port=5900)   