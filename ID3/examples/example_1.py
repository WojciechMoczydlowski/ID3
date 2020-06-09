# author: Jan Piotrowski, Wojciech Moczydlowski
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
from ID3.data.data_controller import get_dataset
from ID3.analize.averaged_results import get_averaged_results_of_k_cross_validation
from ID3.config import FILE


def example_1():
    dataset = get_dataset(FILE)
    target_attribute = "class"

    dataset = shuffle(dataset)

    k_min = 2
    k_max = 10

    def curried_get_averaged_results_of_k_cross_validation_for_dataset(df):
        return get_averaged_results_of_k_cross_validation(df, target_attribute, k_min, k_max)

    results = curried_get_averaged_results_of_k_cross_validation_for_dataset(dataset)

    def round_to_three(number):
        return round(number, 3)
    print(results)
    results = list(map(round_to_three, results))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [i for i in range(k_min, k_max+1)]
    plt.plot(x, results, 'r^')

    plt.xlabel('k in k-cross validation')
    plt.ylabel('accuracy of model')

    for i, j in zip([i for i in x], results):
        ax.annotate(str(j), xy=(i, j), xytext=(10, -10), textcoords='offset points')
    plt.show()
    print(results)


example_1()
