import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity


class UserRecommendations(object):
    with open("data/model.pkl") as f_un:
        model = pickle.load(f_un)

    def __init__(self, model):
        self.model = model

    def get_similarity_matrix(user_matrix):
        user_matrix_sparse = sparse.csr_matrix(user_matrix)
        similarities = cosine_similarity(user_matrix_sparse)
        return similarities

    def get_similar_users(new_user,existing_users,num_users=5):
        new_matrix = np.append(new_user,existing_users,axis=0)
        sim_matrix = get_similarity_matrix(new_matrix)
        top_similar_users = np.argsort(sim_matrix[0])[::-1][1:num_users+1]
        top_similar_users
        return top_similar_users

if __name__ == "__main__":
    pass
