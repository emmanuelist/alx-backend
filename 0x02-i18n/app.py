#!/usr/bin/env python3

"""
Module for a simple Flask web application with user login mock.

This module defines a Flask application that serves a single page,
the index page, and mocks user login functionality.
"""

from datetime import datetime

import pytz
from flask import Flask, g, render_template, request
from flask_babel import Babel, _
from pytz.exceptions import UnknownTimeZoneError


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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Get a user dictionary based on the login_as URL parameter.

    Returns:
        dict: The user dictionary if found, otherwise None.
    """
    try:
        user_id = int(request.args.get("login_as"))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """
    Function to be executed before each request.

    This function sets the user in flask.g if a valid user is found.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match with our supported languages.

    This function is used to select the best language to
    use based on the client's Accept-Language header or
    the 'locale' URL parameter.

    Returns:
        str: The best matching language code (e.g. "en", "fr").

    Example:
        >>> get_locale()
        "en"
    """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if g.user and g.user.get("locale") in app.config["LANGUAGES"]:
        return g.user["locale"]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """
    Determine the best match for the user's timezone.

    This function is used to select the best timezone to
    use based on the 'timezone' URL parameter or the user's
    settings.

    Returns:
        str: The best matching timezone (e.g. "Europe/Paris").

    Example:
        >>> get_timezone()
        "UTC"
    """
    timezone = request.args.get("timezone")
    if timezone:
        try:
            return pytz.timezone(timezone).zone
        except UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get("timezone")
        if user_timezone:
            try:
                return pytz.timezone(user_timezone).zone
            except UnknownTimeZoneError:
                pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


@app.route("/")
def index():
    """Route for the index page."""
    current_time = datetime.now(pytz.timezone(get_timezone())).strftime(
        "%b %d, %Y, %I:%M:%S %p"
    )
    return render_template(
        "index.html",
        title=_("home_title"),
        header=_("home_header"),
        current_time=current_time,
    )


if __name__ == "__main__":
    """
    Run the Flask application in debug mode.

    This code is executed when the script is run directly
    (i.e., not imported as a module).
    """
    app.run(debug=True)
