import threading
import subprocess
import uuid
from flask import Flask
from flask import render_template, url_for, abort, jsonify, request
app = Flask(__name__)

background_scripts = {}

def run_script(user_name):
    subprocess.call(["./generate_pdf.py", "--username=" + user_name, "--own", "--index", "--no_cache", "--output=./templates/" + user_name + ".html"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    user_name = request.form['user_name']
    run_script(user_name)
    return render_template(user_name + '.html')

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)