import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pyspark
from pyspark.mllib.recommendation import MatrixFactorizationModel
import clean_questionnaire_answers as qa
import equipdata as ed

spark = pyspark.sql.SparkSession.builder.getOrCreate()
sc = spark.sparkContext
model = MatrixFactorizationModel.load(sc, "data/firstmodel")
# model = MatrixFactorizationModel.load(sc, "data/secondmodel")
# model = MatrixFactorizationModel.load(sc, "data/thirdmodel")


def generate_new_user_matrix(user_answers,user_total):
    user_answer_ids = qa.get_user_input_ids(user_answers)
    blank_user_df = user_total.iloc[[0]].replace(1,0)
    rand_items = np.array(user_answer_ids)
    for item in rand_items:
        if item in user_total.columns:
            blank_user_df[item] = 1.0
    new_user_matrix = blank_user_df.as_matrix()
    return new_user_matrix

def get_similarity_matrix(new_user_matrix):
    user_matrix_sparse = sparse.csr_matrix(new_user_matrix)
    similarities = cosine_similarity(user_matrix_sparse)
    return similarities

def get_mapping_ids(user_total):
    index_list = []
    for x in range(user_total.shape[0]):
        index_list.append(x)
    mapping_ids = zip(user_total.index,index_list)
    return mapping_ids

def map_user_id(index,mapping_ids):
    for x,y in mapping_ids:
        if index == y:
            return x

def get_top_user_ids(top_similar_users,mapping_ids):
    top_list = []
    for num in top_similar_users:
        top_list.append(map_user_id(num,mapping_ids))
    return top_list

def get_similar_users(user_answers,num_users=5):
    user_total, total_matrix = ed.clean_similarity_data()
    user_matrix = generate_new_user_matrix(user_answers,user_total)
    combined_matrix = np.append(user_matrix,total_matrix,axis=0)
    sim_matrix = get_similarity_matrix(combined_matrix)
    top_similar_users = np.argsort(sim_matrix[0])[::-1][1:num_users+1]
    mapping_ids = get_mapping_ids(user_total)
    top_similar_users = get_top_user_ids(top_similar_users,mapping_ids)
    return top_similar_users

def get_rec_list(top_similar_users,model,num_recs=5):
    rec_list = []
    user_item_df = ed.get_similarity_data()
    for num in top_similar_users:
        try:
            if num in user_item_df.user.unique():
                recs = model.recommendProducts(num,num_recs)
            for rec in recs:
                rec_list.append(rec)
        except:
            continue
    return rec_list

def get_ranked_recommendations(top_similar_users,model,num_recs=5):
    recommendations = []
    rating = []
    rec_list = get_rec_list(top_similar_users,model,num_recs)
    for x,y,z in rec_list:
        if y not in recommendations:
            recommendations.append(y)
            rating.append(z)
    recs_df = pd.DataFrame({'Pedal':recommendations,'Rating':rating})
    recs_df['Rating'] = recs_df['Rating'].astype(float)
    recs_df = recs_df.sort_values('Rating',ascending=False)
    return recs_df

def get_item_name(pedal_id):
    item_ids = qa.mapping_data()
    for item_id,item in item_ids:
        if pedal_id == item_id:
            return item

def get_pedal_list(recs_df,user_answer_ids):
    pedal_list = []
    for rec_id in recs_df['Pedal']:
        if rec_id not in user_answer_ids:
            pedal_list.append(get_item_name(rec_id))
    return pedal_list

def get_recommendations_df(pedal_data,recs_df,user_answer_ids):
    recommendations_df = pedal_data[pedal_data['cleaned_name'].isin(get_pedal_list(recs_df,user_answer_ids))]
    recommendations_df = recommendations_df.drop('cleaned_name',axis=1)
    return recommendations_df
