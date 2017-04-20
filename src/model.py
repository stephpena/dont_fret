import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
import pyspark
from pyspark.mllib.recommendation import MatrixFactorizationModel
import clean_questionnaire_answers as qa
import equipdata as ed

class UserRecommendations(object):

    def __init__(self, user_answers):
        spark = pyspark.sql.SparkSession.builder.getOrCreate()
        sc = spark.sparkContext
        self.model = MatrixFactorizationModel.load(sc, "data/firstmodel")
        self.user_answers = qa.get_user_input_ids(user_answers)
        self.user_total, self.total_matrix = ed.clean_similarity_data()
        self.table_data = ed.cleaned_pedal_data()

    def generate_new_user_matrix(self):
        blank_user_df = self.user_total.iloc[[0]].replace(1,0)
        rand_items = np.array(self.user_answers)
        for item in rand_items:
            blank_user_df[item] = 1.0
        new_matrix = blank_user_df.as_matrix()
        return new_matrix

    def get_similarity_matrix(self,user_matrix):
        user_matrix_sparse = sparse.csr_matrix(user_matrix)
        similarities = cosine_similarity(user_matrix_sparse)
        return similarities

    def get_similar_users(self,num_users=5):
        new_user = self.generate_new_user_matrix()
        combined_matrix = np.append(new_user,self.total_matrix,axis=0)
        sim_matrix = get_similarity_matrix(combined_matrix)
        top_similar_users = np.argsort(sim_matrix[0])[::-1][1:num_users+1]
        return top_similar_users

    def get_rec_list(self):
        rec_list = []
        top_similar_users = self.get_similar_users()
        for num in top_similar_users:
            if num in user_item_df.user.unique():
                recs = model.recommendProducts(num,5)
            for rec in recs:
                rec_list.append(rec)
        return rec_list

    def get_ranked_recommendations(self):
        recommendations = []
        rating = []
        rec_list = self.get_rec_list()
        for x,y,z in rec_list:
            if y not in recommendations:
                recommendations.append(y)
                rating.append(z)
        recs_df = pd.DataFrame({'Pedal':recommendations,'Rating':rating})
        recs_df['Rating'] = recs_df['Rating'].astype(float)
        recs_df = recs_df.sort_values('Rating',ascending=False)
        return recs_df

    def get_item_name(self,pedal_id):
        item_ids = qa.mapping_data()
        for item_id,item in item_ids:
            if pedal_id == item_id:
                return item

    def get_pedal_list(self):
        pedal_list = []
        recs_df = self.get_ranked_recommendations()
        for rec_id in recs_df['Pedal']:
            if rec_id not in self.user_answers:
                pedal_list.append(self.get_item_name(rec_id))
        return pedal_list

    def get_recommendations_df(self):
        recommendations_df = self.table_data[self.table_data['cleaned_name'].isin(self.get_pedal_list())]
        recommendations_df = recommendations_df.drop('cleaned_name',axis=1)
        return recommendations_df

if __name__ == "__main__":
    recommendations_df = get_recommendations_df()
    # return recommendations_df
