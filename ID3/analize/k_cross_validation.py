# author: Jan Piotrowski, Wojciech Moczydlowski
from copy import deepcopy
import numpy as np
import pandas as pd
from sklearn.utils import shuffle
from ID3.model.id3 import id3
from ID3.model.get_target_attribute_of_item import check_if_target_attribute_prediction_is_properly


def k_cross_validation(df, k, target_attribute):
    df = shuffle(df)
    number_of_rows = len(df.index)
    number_of_proper_predict = 0
    original_list_of_subsets = np.array_split(df, k)
    for i in range(k):
        list_of_subsets = deepcopy(original_list_of_subsets)
        testing_subset = deepcopy(list_of_subsets[i])
        del(list_of_subsets[i])

        training_set = pd.concat(list_of_subsets)
        remaining_attributes = training_set.keys().drop(target_attribute)
        root = id3(training_set, remaining_attributes, target_attribute)

        for index, row in testing_subset.iterrows():
            if check_if_target_attribute_prediction_is_properly(row, target_attribute, root):
                number_of_proper_predict += 1

    return number_of_proper_predict/number_of_rows
