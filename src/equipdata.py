import pandas as pd
import numpy as np
import json

def decode_text(list_name):
    a = []
    for x in list_name:
        a.append(x.decode('utf-8'))
    return a

with open('data/artist_df.csv') as f:
    artist_df = pd.read_csv(f)
artist_names = list(artist_df['artist_name'])
artist_names = decode_text(artist_names)

with open('data/cleaned_pedal_data.csv') as f:
    pedal_data = pd.read_csv(f)
with open('data/artist_data.json') as f:
    artist_data = json.load(f)

clean_pedal_data = pedal_data.drop('equipment_name',axis=1)
clean_pedal_data = clean_pedal_data.drop_duplicates()
clean_pedal_data.reset_index(drop=True,inplace=True)

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


with open('data/artist_style.csv') as f:
    artist_style_df = pd.read_csv(f)

with open('data/artist_owned.csv') as f:
    artist_owned_df = pd.read_csv(f)

with open('data/user_style_df.csv') as f:
    user_style_df = pd.read_csv(f)
    user_style_df = user_style_df.astype(int)
with open('data/user_item_df.csv') as f:
    user_item_df = pd.read_csv(f)
    user_item_df = user_item_df.astype(int)

#reshape data into matrix for cosine similarity calc
user_style_pivot = user_style_df.pivot(index='user',columns='item')
user_style_pivot = user_style_pivot.fillna(0)
user_style_pivot.columns = user_style_pivot.columns.droplevel(0)
# user_style_matrix = user_style_pivot.as_matrix()
# user_style_matrix = user_style_matrix

#update dataframe to include 0s for items they do not own
user_item_pivot = user_item_df.pivot(index='user',columns='item')
user_item_pivot = user_item_pivot.fillna(0)
user_item_pivot.columns = user_item_pivot.columns.droplevel(0)
user_item_pivot['user'] = user_item_pivot.index
full_user_item_df = pd.melt(user_item_pivot, id_vars='user', value_vars=list(user_item_pivot.columns[:2500]),
            var_name='item', value_name='rating')
