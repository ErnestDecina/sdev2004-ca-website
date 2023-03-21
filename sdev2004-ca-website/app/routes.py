#
#   routes.py
#
#   Description:
#       Controls what is given back to client when URL is requested
#
#
#   Authors:
#       Daniel Wu          (C21460524)
#       Alex Tsang         (C21751999)
#       Sean Tighe         (C21329431)
#       Micheal O'Brien    (C21502889)
#       Ernest John Decina (C21394933)
#

# Dependencies
from app import app
from flask import render_template
from flask import redirect, request
from app.utils import get_locale


@app.route('/')
@app.route('/index')
def index():
    """Landing page users will land at"""
    return render_template("index.html")
# End def index()


# Set Language
@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    """Change the language code within the users cookies and reserve them the website"""
    change_lang_code(lang_code)
    return redirect(request.referrer)
# End def set_language()
