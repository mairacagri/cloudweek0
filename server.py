from flask import Flask, render_template
from random import randint
from time import time

app = Flask(__name__)


@app.route("/")
def homepage():
    current_epoch = time()
    random_number = randint(0, 1000)

    return render_template("homepage.html", number=random_number, time=current_epoch)
