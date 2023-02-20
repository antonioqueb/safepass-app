from flask import Flask, jsonify, request
import os
import secrets

app = Flask(__name__)

@app.route('/')
def generate_password():
    password = secrets.token_hex(16)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
