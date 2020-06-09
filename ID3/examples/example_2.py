# author: Jan Piotrowski, Wojciech Moczydlowski
import matplotlib.pyplot as plt
import numpy as np
from sklearn.utils import shuffle
from ID3.data.data_controller import get_dataset
from ID3.analize.averaged_results import get_averaged_results_of_k_cross_validation
from ID3.config import FILE


def example_2():
    dataset = get_dataset(FILE)
    target_attribute = "class"

    dataset.sample(frac=1)

    k_min = 2
    k_max = 10

    def curried_get_averaged_results_of_k_cross_validation_for_dataset(df):
        return get_averaged_results_of_k_cross_validation(df, target_attribute, k_min, k_max)

    results_for_full_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(dataset)

    dataset = shuffle(dataset)
    half_of_dataset = np.array_split(dataset, 2)[0]
    results_for_half_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(half_of_dataset)

    dataset = shuffle(dataset)
    one_third_of_dataset = np.array_split(dataset, 3)[0]
    results_for_one_third_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(one_third_of_dataset)

    dataset = shuffle(dataset)
    quarter_of_dataset = np.array_split(dataset, 4)[0]
    results_for_quarter_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(quarter_of_dataset)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [i for i in range(k_min, k_max+1)]
    plt.plot(x, results_for_full_dataset, 'r^')
    plt.plot(x, results_for_half_of_dataset, 'go')
    plt.plot(x, results_for_one_third_of_dataset, 'bs')
    plt.plot(x, results_for_quarter_of_dataset, 'rs')

    plt.xlabel('k in k-cross validation')
    plt.ylabel('accuracy of model')
    plt.show()


example_2()
