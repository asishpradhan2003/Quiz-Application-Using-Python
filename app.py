from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_quiz')
def start_quiz():
    subprocess.Popen(['python', 'main.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
