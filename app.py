from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import json
import sys
import cPickle as pickle
import requests
import src.model as m
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

#
# @app.route('/answers', methods=['POST'])
# def test():
#     return render_template('test.html')

@app.route('/answers', methods=['POST','GET'])
def answers():
    # user_data = request.json
    # a, b, c = user_data['a'], user_data['b'], user_data['c']
    # root_1, root_2 = _solve_quadratic(a, b, c)
    test_1 = 25
    test_2 = 15
    return jsonify({'test_1': test_1, 'test_2': test_2})


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
    df.columns = ['Brand','Pedal','Category','Instrument','Equipboard URL']
    return df

def get_recommendations(answers):
    top_sim_users = m.get_similar_users(answers,num_users=25)
    recs_df = m.get_ranked_recommendations(top_sim_users,m.model)
    cleaned_pedal_data = m.ed.cleaned_pedal_data()
    user_answer_ids = m.qa.get_user_input_ids(answers)
    recs = m.get_recommendations_df(cleaned_pedal_data,recs_df,user_answer_ids)
    return recs



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
