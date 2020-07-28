from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
        return "<h1 style='color:blue'>Hello world</h1>"

@app.route("/db")
def test_db():
        return "<h1>{}</h1>".format(os.environ.get("DATABSE_URL"))

if __name__ == "__main__":
        app.run(host='0.0.0.0')
