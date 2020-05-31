from ID3.data.data_controller import DataController
from ID3.model.id3 import id3
from ID3.view.view import pretty_print_tree


def main():
    data_controller = DataController()

    dataset = data_controller.get_dataset()
    target_attribute = "class"
    remaining_attributes = data_controller.get_remaining_attributes()

    root = id3(dataset, remaining_attributes, target_attribute)

    pretty_print_tree(root)


if __name__ == '__main__':
    main()