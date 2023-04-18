#
#   __init__.py
#
#   Description:
#       __init__ for package: app
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
from flask import Flask, session
from flask_babel import Babel
from app.utils import get_locale

# Create the flask app
app = Flask(__name__)

# If we are using session then we need to set a secret key
app.secret_key = 'Our super duper secret key'

# Hook Babel into your app
babel = Babel(app)

# Initiate the Babel app passing through the locale you want to start with
babel.init_app(app, locale_selector=get_locale)

from app import routes
