from flask import Flask, render_template
import secrets

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', password=secrets.token_hex(16))

@app.route('/generate-password')
def generate_password():
    password = secrets.token_hex(16)
    return {'password': password}

if __name__ == '__main__':
    app.run(debug=True)
