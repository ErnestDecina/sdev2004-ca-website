#
#   __init__.py
#
#   Description:
#       __init__ for package: util
#
#
#   Authors:
#       Daniel Wu          (C21460524)
#       Alex Tsang         (C21751999)
#       Sean Tighe         (C21329431)
#       Micheal O'Brien    (C21502889)
#       Ernest John Decina (C21394933)
#       Ron Pingol         (C21782059)
#

# Dependencies
from flask import session


def get_locale():
    """Returns the current 2-letter language code stored else set english to default"""
    if 'language' in session:
        return session['language']
    else:
        session['language'] = 'en'
    return session['language']


def change_lang_code(lang_code):
    """Changes the current session language"""
    session.pop('language', lang_code)
    session["language"] = lang_code


def start_lang_session_code():
    """Starts the app in the language english"""
    if session.get("language") is None:
        session["language"] = 'en'
