import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/dontfret', methods=['GET'])
def pedal():
    df = get_data()
    df = df.to_html(index=False)
    df = df.replace('class="dataframe">','id="data-types" class="dataframe>"')
    return render_template('pedal.html',tables=[df])
# @app.route('/test', methods=['GET'])
# def test():
#     return render_template('test.html')

def get_data():
    with open('data/cleaned_pedal_data.csv') as f:
        pedal_data = pd.read_csv(f)
    clean_pedal_data = pedal_data.drop('equipment_name',axis=1)
    clean_pedal_data = clean_pedal_data.drop_duplicates()
    clean_pedal_data.reset_index(drop=True,inplace=True)
    # table_df = clean_pedal_data.drop('cleaned_name',axis=1)
    table_df = clean_pedal_data
    table_df['equipment_url'] = 'http://equipboard.com' + table_df['equipment_urls']
    table_df = table_df.drop('equipment_urls',axis=1)
    # df = table_df.iloc[100:200]
    pedal_list = ['TC Electronic Ditto Looper Limited Gold Edition',
     'Ibanez TS9 Tube Screamer',
     'EarthQuaker Devices Ghost Echo Reverb',
     'TC Electronic Hall Of Fame Reverb',
     'Strymon El Capistan dTape Echo Delay',
     'Voodoo Lab Power 2 Plus',
     'Line 6 POD HD500',
     'Roger Mayer Voodoo Vibe',
     'Moog Minifooger MF Chorus',
     'Boss DD-3 Digital Delay',
     'MXR M108 Ten Band Graphic Equalizer',
     'Musonic VP100 Phaser',
     'Boss TU-3 Chromatic Tuner',
     'Top Tone Drivegate DG1',
     'Electro-Harmonix Micro POG',
     'Fulltone OCD Obsessive Compulsive Drive Overdrive',
     'Empress Compressor']
    df = table_df[table_df['cleaned_name'].isin(pedal_list)]
    df = df.drop('cleaned_name',axis=1)
    df = df.rename({'brand_name': 'Brand','product_name': 'Pedal','product_category': 'Category','instrument_type': 'Instrument','equipment_url': 'Equipboard URL'})
    return df


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
