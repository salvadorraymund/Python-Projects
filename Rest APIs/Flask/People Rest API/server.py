import sys
sys.path.append(
    "/Users/raysal/Documents/Python Projects/Rest APIs/Flask/People Rest API/.venv/lib/python3.9/site-packages")
from flask import render_template
import connexion


# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# read the swagger.yml file to configure the endpoints
app.add_api("swagger.yml")


# Create a URL route in our application for "/"
@app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


# If we're running in a stand alone mode, run the application
if __name__ == "__main__":
    app.run(debug=True)
