from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Aula Devops"

@app.route("/health")
def health():
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['APP_PORT'], debug=True)
