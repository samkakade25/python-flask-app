from flask import Flask, request, jsonify, has_request_context
import logging
from concurrent_log_handler import ConcurrentTimedRotatingFileHandler
import os
import zipfile
from os.path import basename

log_dir1 = 'Accesslogs'
if not os.path.exists(log_dir1):
    os.makedirs(log_dir1)

log_dir2 = 'Errorlogs'
if not os.path.exists(log_dir2):
    os.makedirs(log_dir2)



# Custom Formatter to include URL and Remote Address in the log
class NewFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote = request.remote_addr
        else:
            record.url = None
            record.remote = None
        return super().format(record)

# zip file creation    
def rotator(source, dest):
    # rotated log file is zipped and the original log file will be deleted 
    zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED).write(
        source, basename(source))
    os.remove(source)


access_handler = ConcurrentTimedRotatingFileHandler(os.path.join(log_dir1, 'access.log'), when="w0", interval=1, backupCount=100, maxBytes=10*1024*1024)
access_handler.setLevel(logging.INFO)
access_handler.namer = lambda name: name.replace(".log", "") + ".zip"

error_handler = ConcurrentTimedRotatingFileHandler(os.path.join(log_dir2, 'error.log'), when="midnight", interval=1, backupCount=100, maxBytes=10*1024*1024)
error_handler.setLevel(logging.ERROR)
error_handler.namer = lambda name: name.replace(".log", "") + ".zip"
errorFormatter = NewFormatter("%(asctime)s - %(url)s - %(remote)s - [%(levelname)s] - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
error_handler.setFormatter(errorFormatter)


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