# author: Jan Piotrowski, Wojciech Moczydlowski
import random
import statistics
from ID3.analize.k_cross_validation import k_cross_validation


def get_averaged_results_of_k_cross_validation(df, target_attribute, k_min, k_max):
    results = []
    for j in range(25):
        print(j)
        random.seed(j)
        df.sample(frac=1)
        results.append([])
        for i in range(k_min, k_max + 1):
            results[j].append(k_cross_validation(df, i, target_attribute))

    temp_results = [[] for i in range(len(results[0]))]
    for i in range(len(results[0])):
        for cell in results:
            temp_results[i].append(cell[i])
    return list(map(statistics.mean, temp_results))
