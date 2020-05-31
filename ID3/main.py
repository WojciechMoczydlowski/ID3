from ID3.data.data_controller import get_dataset
from ID3.model.id3 import id3
from ID3.view.view import pretty_print_tree


def main():

    dataset = get_dataset("C:/Users/HP/PycharmProjects/ID3/ID3/data/mushrooms.csv")
    target_attribute = "class"
    remaining_attributes = dataset.keys().drop("class")

    root = id3(dataset, remaining_attributes, target_attribute)

    pretty_print_tree(root)


if __name__ == '__main__':
    main()