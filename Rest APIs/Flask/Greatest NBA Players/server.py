"""
Main module of the program
"""
# import sys
# sys.path.append(
#     "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/Greatest NBA Players/.venv/lib/python3.9/site-packages")
from flask import render_template
import config

connex_app = config.connex_app
connex_app.add_api('swagger.yml')


@connex_app.route('/')
def home():
    """
    This function responds to the browser URL localhost:5000/
    :return: the rendered template 'home.html'
    """
    return render_template('home.html')


if __name__ == "__main__":
    connex_app.run(debug=True)
