from flask import Flask
import os

app = Flask(__name__)

@app.route('/health_check')
def health_check():
    return 'OK'

@app.route('/')
def index():
    return 'index'

if __name__ == "__main__":
    PORT = os.environ.get("PORT", 8080)
    app.run('0.0.0.0', PORT, debug=True)
