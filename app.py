from flask import Flask, render_template, redirect
from detect_lipstick import detect_lip_color

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start')
def start_detection():
    detect_lip_color()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
