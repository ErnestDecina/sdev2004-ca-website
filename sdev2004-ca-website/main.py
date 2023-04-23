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
import os
from app import app
from waitress import serve

# Start Flask Application
if __name__ == "__main__":
    print("App running on http://localhost:")
    app.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 5000)))
    # serve(app, listen="*:5000")
