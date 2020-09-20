from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/flop')
def landing_page():
    return render_template("index.html")
