from __future__ import division
from math import sqrt
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dontfret', methods=['GET'])
def pedal():
    return render_template('pedal.html')

def brand_list():
    brands = ["Boss","Korg","Electro-Harmonix","Budda","Blackstar","Bogner","Digitech","Fulltone","Dunlop"]
    return brands
brands = brand_list()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
