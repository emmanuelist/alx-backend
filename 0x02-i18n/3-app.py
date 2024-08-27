#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration for Flask app.

    This class defines the configuration settings for the Flask application.

    Attributes:
        LANGUAGES (list): A list of supported languages.
        Defaults to ["en", "fr"].
        BABEL_DEFAULT_LOCALE (str): The default locale to use.
        Defaults to "en".
        BABEL_DEFAULT_TIMEZONE (str): The default timezone to use.
        Defaults to "UTC".
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.

    This function is used to select the best language to
    use based on the client's Accept-Language header.

    Returns:
        str: The best matching language code (e.g. "en", "fr").

    Example:
        >>> get_locale()
        "en"
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """Route for the index page."""
    return render_template(
        "3-index.html", title=_("home_title"), header=_("home_header")
    )


if __name__ == "__main__":
    """
    Return the Flask application in debug mode.

    This code is executed when the root URL is accessed.
    """
    app.run(debug=True)
