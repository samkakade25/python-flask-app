from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World", 200

@app.route('/error')
def error_endpoint():
    app.logger.error("Error logged at /error endpont")
    return jsonify({"error": "Bad Request"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)