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

    dataset = shuffle(dataset)
    one_eight_of_dataset = np.array_split(dataset, 8)[0]
    one_eight_for_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(one_eight_of_dataset)

    dataset = shuffle(dataset)
    one_sixteen_of_dataset = np.array_split(dataset, 16)[0]
    one_sixteen_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(one_sixteen_of_dataset)

    dataset = shuffle(dataset)
    one_thirty_two_of_dataset = np.array_split(dataset, 32)[0]
    one_thirty_two_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(one_thirty_two_of_dataset)

    dataset = shuffle(dataset)
    one_sixty_four_of_dataset = np.array_split(dataset, 64)[0]
    one_sixty_four_of_dataset = curried_get_averaged_results_of_k_cross_validation_for_dataset(one_sixty_four_of_dataset)

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [i for i in range(k_min, k_max+1)]
    plt.plot(x, one_sixty_four_of_dataset, 'r^')
    plt.plot(x, one_eight_for_dataset, 'go')
    plt.plot(x, one_sixteen_of_dataset, 'bs')
    plt.plot(x, one_thirty_two_of_dataset, 'rs')

    plt.xlabel('k in k-cross validation')
    plt.ylabel('accuracy of model')
    plt.show()


example_2()
