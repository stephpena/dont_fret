import numpy as np
import pandas as pd
import equipdata as ed


def add_ids(input_list):
    id_list = []
    for i,a in enumerate(input_list):
        id_list.append([i,a])
    return id_list

def mapping_data():
    genres,similars,pedals = ed.get_item_lists()
    item_mappings = add_ids(pedals + genres + similars)
    return item_mappings

def get_item_id(answer,item_mappings):
    for item_id,item_name in item_mapping:
        if answer == y:
            return item_id

def get_user_input_ids(answers):
    answer_ids = []
    for answer in answers:
        answer_ids.append(get_item_id(answer))
    return answer_ids
