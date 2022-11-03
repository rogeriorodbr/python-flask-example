from flask import Flask, jsonify
from multiprocessing import Value
import os

counter = Value('i', 0)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Aula Devops"

@app.route("/health")
def health():
    return "200"

@app.route('/counter')
def index():
    with counter.get_lock():
        counter.value += 1
        # save the value ASAP rather than passing to jsonify
        # to keep lock time short
        unique_count = counter.value

    return str(unique_count)
    
    return "200"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['APP_PORT'], debug=True)
