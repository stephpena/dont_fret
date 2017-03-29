import pandas as pd
import numpy as np
import json

def decode_text(list_name):
    a = []
    for x in list_name:
        a.append(x.decode('utf-8'))
    return a

def import_files(filename,format):
    with open(filename) as f:
        if format == 'csv':
            file_data = pd.read_csv(f)
        else:
            file_data = json.load(f)
    return file_data

def cleaned_pedal_data():
    pedal_data = import_files('data/cleaned_pedal_data.csv','csv')
    clean_pedal_data = pedal_data.drop('equipment_name',axis=1)
    clean_pedal_data = clean_pedal_data.drop_duplicates()
    clean_pedal_data.reset_index(drop=True,inplace=True)
    return clean_pedal_data

def get_item_lists():
    artist_data = import_files('data/artist_data.json','json')
    fix = [u'Blues',
     u'Brass & Military',
     u"Children's",
     u'Classical',
     u'Electronic & DJ',
     u'Folk, World, & Country',
     u'Funk / Soul',
     u'Hip Hop',
     u'Jazz',
     u'Latin',
     u'Non-Music',
     u'Orchestra',
     u'Pop',
     u'Reggae',
     u'Rock',
     u'Stage & Screen',
     u'Unknown']

    genres = []
    similars = []
    for key1,value2 in artist_data.iteritems():
        for key2,value2 in value2.iteritems():
    #         if fix_name in value2 and key2 == 'genres':
    #             fix.append(key1)
            for x in value2:
                if key2 == 'genres' and x in fix:
                    genres.append(x)
                elif key2 == 'similar artists' or key2 == 'member of':
                    similars.append(x)
    genres = list(set(genres))
    similars = list(set(similars))
    pedals = list(set(clean_pedal_data['cleaned_name']))
    return (genres,similars,pedals)

with open('data/artist_style.csv') as f:
    artist_style_df = pd.read_csv(f)

with open('data/artist_owned.csv') as f:
    artist_owned_df = pd.read_csv(f)


def get_similarity_data():
    with open('data/user_total_df.csv') as f:
        user_total_df =  pd.read_csv(f)
    user_total_df = user_total_df.astype(int)
    return user_total_df

def clean_similarity_data():
    user_total_df = get_similarity_data()
    user_total_pivot = user_total_df.pivot(index='user',columns='item')
    user_total_pivot = user_total_pivot.fillna(0)
    user_total_pivot.columns = user_total_pivot.columns.droplevel(0)
    user_total_matrix = user_total_pivot.as_matrix()
    return (user_total_pivot,user_total_matrix)
