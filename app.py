from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os

log_file_path = 'app.log'
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w'):
        pass 

handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=5)
handler.setLevel(logging.INFO)

app = Flask(__name__)

app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

@app.route('/')
def hello_world():
    app.logger.info("Hello World endpoint was reached successfully")
    return "Hello World", 200
    

@app.route('/error')
def error_endpoint():
    app.logger.error("Error logged at /error endpont")
    return jsonify({"error": "Bad Request"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)