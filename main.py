from flask import Flask, render_template

webapp = Flask(__name__)


@webapp.route("/")
def index():
    return render_template("index.html")


@webapp.route("/about_me")
def about_me():
    return render_template("about.html")


@webapp.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@webapp.route("/portfolio/fakebook")
def portfolio_fakebook():
    return render_template("portfolio/fakebook.html")


@webapp.route("/portfolio/boogle")
def portfolio_boogle():
    return render_template("portfolio/boogle.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    webapp.run(use_reloader=True)
