from datetime import datetime
from flask import Flask, render_template, request

webapp = Flask(__name__)


@webapp.route("/")
def index():
    name = "Jörg"
    return render_template("index.html", name=name, date=datetime.now())


@webapp.route("/about", methods=["GET"])
def about():
    return render_template("about.html")


@webapp.route("/about", methods=["POST"])
def contact():
    contact_name = request.form.get("contact_name")
    contact_email = request.form.get("contact_email")
    contact_message = request.form.get("contact_message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    return render_template("success.html")


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
