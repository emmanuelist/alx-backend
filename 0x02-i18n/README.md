# 0x02. i18n

## Project Overview

This project focuses on implementing internationalization (i18n) in a Flask application using the Flask-Babel extension. The project will involve setting up a basic Flask application, configuring Babel for language support, and enabling localization features such as language selection based on user preferences, URL parameters, or request headers. Additionally, the project includes timezone localization and displaying localized timestamps.

## Learning Objectives

- Parametrizing Flask templates to support multiple languages.
- Inferring the correct locale from URL parameters, user settings, or request headers.
- Localizing timestamps based on the user's timezone.

## Resources

To complete this project, you can refer to the following resources:

- [Flask-Babel Documentation](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
- [pytz Documentation](https://pytz.sourceforge.net/)

## Requirements

- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- A `README.md` file at the root of the project directory is mandatory.
- Code must adhere to the `pycodestyle` style (version 2.5).
- The first line of all Python files should be exactly `#!/usr/bin/env python3`.
- All `.py` files should be executable.
- All modules, classes, functions, and methods should have proper documentation.
- All functions and coroutines must be type-annotated.

## Project Structure

The project is divided into the following tasks:

### 1. Basic Flask App

**Task:** Set up a basic Flask application with a single `/` route and an index template that displays a simple message.

**Files:**

- `0-app.py`
- `templates/0-index.html`

### 2. Basic Babel Setup

**Task:** Install and configure the Babel extension in the Flask app. Define available languages and set default locale and timezone.

**Files:**

- `1-app.py`
- `templates/1-index.html`

### 3. Get Locale from Request

**Task:** Create a function to determine the best language match from the request headers using `request.accept_languages`.

**Files:**

- `2-app.py`
- `templates/2-index.html`

### 4. Parametrize Templates

**Task:** Use the `_` or `gettext` function to parametrize templates for different languages. Set up translation files and compile them.

**Files:**

- `3-app.py`
- `babel.cfg`
- `templates/3-index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`
- `translations/en/LC_MESSAGES/messages.mo`
- `translations/fr/LC_MESSAGES/messages.mo`

### 5. Force Locale with URL Parameter

**Task:** Implement a feature to force a specific locale by passing a `locale` parameter in the URL.

**Files:**

- `4-app.py`
- `templates/4-index.html`

### 6. Mock Logging In

**Task:** Mock a login system using a user table and display localized messages based on user login status.

**Files:**

- `5-app.py`
- `templates/5-index.html`

### 7. Use User Locale

**Task:** Update the `get_locale` function to use a user’s preferred locale if available.

**Files:**

- `6-app.py`
- `templates/6-index.html`

### 8. Infer Appropriate Time Zone

**Task:** Create a function to infer the user's timezone from the URL, user settings, or default to UTC, and validate it.

**Files:**

- `7-app.py`
- `templates/7-index.html`

### 9. Display the Current Time

**Task:** Display the current time on the homepage based on the inferred timezone.

**Files:**

- `app.py`
- `templates/index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`

## Usage

To run the application, follow these steps:

1. Install the required dependencies:

   ```bash
   pip3 install flask_babel==2.0.0 pytz
   ```

2. Run the Flask application:

   ```bash
   python3 app.py
   ```

3. Access the application via `http://127.0.0.1:5000/` in your web browser.

## Testing

- Ensure that the correct language and timezone settings are applied by visiting the application with different `locale` and `login_as` URL parameters.
- Verify that the translations are correctly displayed based on the user's language preference.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
