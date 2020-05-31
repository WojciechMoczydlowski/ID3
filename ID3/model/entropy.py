import math
import numpy as np


def count_entropy(dataset):

    elements, occurrences = np.unique(dataset, return_counts=True)
    print(elements, occurrences)
    for i in range(len(elements)):
        entropy = np.sum([(-occurrences[i] / np.sum(occurrences)) *
                          np.log2(occurrences[i] / np.sum(occurrences))])
    return (entropy)
