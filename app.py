import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dontfret', methods=['GET'])
def pedal():
    return render_template('pedal.html')

def get_data():
    with open('data/cleaned_pedal_data.csv') as f:
        pedal_data = pd.read_csv(f)
    clean_pedal_data = pedal_data.drop('equipment_name',axis=1)
    clean_pedal_data = clean_pedal_data.drop_duplicates()
    clean_pedal_data.reset_index(drop=True,inplace=True)
    table_df = clean_pedal_data.drop('cleaned_name',axis=1)
    table_df['equipment_url'] = 'http://equipboard.com' + table_df['equipment_urls']
    table_df = table_df.drop('equipment_urls',axis=1)
    df = table_df.head(20)
    return df

df = get_data()
brand_list = list(df['brand_name'])
product_list = list(df['product_name'])
cat_list = list(df['product_category'])
instrument_list = list(df['instrument_type'])
url_list = list(df['equipment_url'])

# options = []
#
# for value in sorted(values.keys()):
#     options.append("<option value='" + value + "'>" + values[value] + "</option>")

@app.route('/')
def brand_list():
    brands = ["Boss","Korg","Electro-Harmonix","Budda","Blackstar","Bogner","Digitech","Fulltone","Dunlop"]
    return brands
brands = brand_list()

def genre_list():
    genres = []
    return genres
genres = genre_list()

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
