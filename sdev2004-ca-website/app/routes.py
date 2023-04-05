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
#       Ron Pingol         (C21782059)
#
# Dependencies
from app import app
from flask import render_template
from flask import redirect, request
from app.utils import change_lang_code, start_lang_session_code


#
# Website landing page
#
#   Authors:
#       Daniel Wu
#       Alex Tsang
#       Sean Tighe
#       Micheal O'Brien
#       Ernest John Decina
#
@app.route('/')
@app.route('/index')
def index():
    """Landing page users will land at"""
    start_lang_session_code()
    return render_template("index.html", country_selector="en")


#
# Korea Home Page
#
# Author: Ernest John Decina
#
@app.route('/ko/home')
def ko_home():
    """Home page of Korea"""
    start_lang_session_code()
    return render_template("home.html", country_selector="ko")


#
# Korea Booking Page
#
# Author: Ron Pingol
#
@app.route('/ko/booking')
def ko_booking():
    """Booking page of Korea"""
    start_lang_session_code()
    return render_template("booking.html", country_selector="ko")


#
# Korea Todo Page
#
# Author: Alex Tsang
#
@app.route('/ko/todo')
def ko_todo():
    """Todo page of Korea"""
    start_lang_session_code()
    return render_template("todo.html", country_selector="ko")


#
# Sweden Home Page
#
# Author: Daniel Wu
#
@app.route('/sv/home')
def sv_home():
    """Home page of Sweeden"""
    start_lang_session_code()
    return render_template("home.html", country_selector="sv")


#
# Sweden Booking Page
#
# Author: Micheal O'Brien
#
@app.route('/sv/booking')
def sv_booking():
    """Booking page of Sweeden"""
    start_lang_session_code()
    return render_template("booking.html", country_selector="sv")


#
# Sweden Todo Page
#
# Author: Seán Tighe
#
@app.route('/sv/todo')
def sv_todo():
    """todo page of Sweeden"""
    start_lang_session_code()
    return render_template("todo.html", country_selector="sv")


# Set Language
@app.route('/setlang/<lang_code>')
def set_language(lang_code):
    """Change the language code within the users cookies and reserve them the website"""
    change_lang_code(lang_code)
    return redirect(request.referrer)
# End def set_language()
