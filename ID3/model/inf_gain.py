# author: Jan Piotrowski, Wojciech Moczydlowski
import math

from ID3.model.entropy import count_entropy
from ID3.model.entropy import count_multiset_entropy


def inf_gain(dataset, remaining_attributes, target_attribute):

    max_gain = -math.inf
    splitting_attribute = remaining_attributes[-1]

    dataset_entropy = count_entropy(dataset)

    for attribute in remaining_attributes:
        tmp_gain = dataset_entropy - count_multiset_entropy(dataset, attribute, target_attribute)

        if tmp_gain > max_gain:
            max_gain = tmp_gain
            splitting_attribute = attribute

    return splitting_attribute

