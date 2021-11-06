from flask import Flask, render_template
from datetime import datetime

webapp = Flask(__name__)


@webapp.route("/")
def index():
    name = "Jörg"
    return render_template("index.html", name=name, date=datetime.now())


@webapp.route("/about")
def about():
    return render_template("about.html")


@webapp.route("/portfolio")
def portfolio():
    projects = ["Flask Project", "Fakebook", "Boogle"]
    return render_template("portfolio.html", projects=projects)


@webapp.route("/portfolio/fakebook")
def portfolio_fakebook():
    return render_template("/portfolio/fakebook.html")


@webapp.route("/portfolio/boogle")
def portfolio_boogle():
    return render_template("/portfolio/boogle.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webapp.run(use_reloader=True)
