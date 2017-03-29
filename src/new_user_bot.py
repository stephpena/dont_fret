"""
Question bot class created to generate random new users.

This class was created to generate random inputs to simulate new users.
It can generate a single user or a matrix of users.

"""

import pandas as pd
import numpy as np
import equipdata as ed

class PedalQuestionBot(object):
# """
# Bot built to generate random results to user questionnaire
# 
# Attributes
# ----------
# user_total_df:
#     The existing user dataframe of users(rows) and items(columns).
#     Items are either pedals, genres, or similar artists
#     Consists of 0 or 1 depending on if the user has the item/genre/artist
# num_users:
#     The number of random new users to generate.
#
# Methods
# -------
# new_user()
# multi_new_user_matrix(num_users)
# """

    def __init__(self):
        self.user_total_df = ed.user_total_pivot()
        self.blank_matrix = self.user_total_df.iloc[[0]].replace(1,0).as_matrix()

    def new_user():
        """Return single new user matrix of random answers to the questionnaire.

        Parameters
        ----------
        None

        Returns
        -------
        new_user: matrix
            The answers of the bot to the questionnaire. 1 = an answer to questionnaire 0 =
            not provided as an item/genre/influence.
        """
        blank_user_df = self.self.blank_matrix.iloc[[0]].replace(1,0)
        rand_pedals = np.random.choice(self.blank_matrix.columns[:2500],np.random.randint(9))
        rand_genres = np.random.choice(self.blank_matrix.columns[2500:2516],np.random.randint(1,3))
        rand_artists = np.random.choice(self.blank_matrix.columns[2516:],np.random.randint(2))
        rand_items = np.append(rand_pedals,(rand_genres,rand_artists))
        for item in rand_items:
            blank_user_df[item] = 1.0
        new_user = blank_user_df.as_matrix()
        return new_user

    def multi_new_user_matrix(num_users=5):
        """Return a multiple new user matrix of random answers to the questionnaire.

        Parameters
        ----------
        num_users:
            The number of new user data to be randomly generated.

        Returns
        -------
        new_user: matrix
            The answers of the bot to the questionnaire. 1 = an answer to questionnaire 0 =
            not provided as an item/genre/influence.
        """
        for i in range(num_times+1):
            if i == 0:
                user_matrix = new_user(self.self.blank_matrix)
            else:
                user_matrix = user_matrix.append(new_user(self.self.blank_matrix))
        return user_matrix

if __name__ == '__main__':
    user_bot = PedalQuestionBot()
    user_bot.new_user()
