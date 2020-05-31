import math
import numpy as np
from ID3.model.utils import attribute_values
from ID3.model.utils import subset_for_attribute


def count_entropy(dataset):
    elements, occurrences = np.unique(dataset, return_counts=True)
    for i in range(len(elements)):
        entropy = np.sum([(-occurrences[i] / np.sum(occurrences)) *
                          np.log2(occurrences[i] / np.sum(occurrences))])
    return entropy


def count_multiset_entropy(dataset, attribute, target_attribute):
    entropy = 0
    values = attribute_values(dataset, attribute)
    dataset_size = len(dataset)

    for value in values:
        subset = subset_for_attribute(dataset, attribute, value)
        subset_size = len(subset)
        class_subset = subset[target_attribute]

        entropy += (subset_size * count_entropy(class_subset)) / dataset_size

    return entropy

