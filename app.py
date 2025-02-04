from flask import Flask, request, jsonify
import logging
from logging.handlers import RotatingFileHandler
import os

log_dir = 'log'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

access_handler = RotatingFileHandler(os.path.join(log_dir, 'access.log'), maxBytes=10000, backupCount=5)
access_handler.setLevel(logging.INFO)
access_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

error_handler = RotatingFileHandler(os.path.join(log_dir, 'error.log'), maxBytes=10000, backupCount=5)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))


app = Flask(__name__)

app.logger.addHandler(error_handler)
app.logger.setLevel(logging.INFO)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.addHandler(access_handler)

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