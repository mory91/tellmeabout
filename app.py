from flask import Flask, render_template, request

from ice_breaker import get_information


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def render_me():
        return render_template("me.html")

    @app.route("/about", methods=["POST"])
    def render_about():
        name = request.form.get("name")
        data, photo = get_information(name)
        return render_template("about.html", data=data, photo=photo)

    return app
