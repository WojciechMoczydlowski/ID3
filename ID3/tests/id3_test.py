# author: Jan Piotrowski, Wojciech Moczydlowski
from ID3.data.data_controller import get_dataset
from ID3.model.id3 import id3
from ID3.model.get_target_attribute_of_item import check_if_target_attribute_prediction_is_properly


def test_id3():
    dataset = get_dataset("/home/janek/Desktop/PSZT/ID3/ID3/mushrooms.csv")
    target_attribute = "class"
    remaining_attributes = dataset.keys().drop("class")

    root = id3(dataset, remaining_attributes, target_attribute)

    for index, row in dataset.iterrows():
        assert check_if_target_attribute_prediction_is_properly(row, 'class', root)
