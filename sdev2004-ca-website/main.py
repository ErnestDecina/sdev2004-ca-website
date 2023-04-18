#
#   main.py
#
#   Description:
#       Software for Global Market 2 Continuous Assessment
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
from waitress import serve

# Start Flask Application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    # serve(app, host="0.0.0.0", port=8080)
