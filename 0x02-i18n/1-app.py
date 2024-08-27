#!/usr/bin/env python3
"""
Module for a simple Flask web application.

This module defines a Flask application that serves a single page,
the index page.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
        Configuration for the Flask application.
        """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """
    Route for the index page.

    Returns:
        str: The rendered HTML template for the index page.

    Example:
        >>> from app import app
        >>> client = app.test_client()
        >>> response = client.get('/')
        >>> response.status_code
        200
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    """Run thee flask application in debug mode

    This code is executed when the script is run directly (i.e., not imported
    as a module)
    """
    app.run(debug=True)
