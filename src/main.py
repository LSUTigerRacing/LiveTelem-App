from flask import Flask, render_template
from api import api

app = Flask(__name__)
app.register_blueprint(api)

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)
