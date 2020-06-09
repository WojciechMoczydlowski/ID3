# author: Jan Piotrowski, Wojciech Moczydlowski
from ID3.model.inf_gain import inf_gain
from ID3.model.utils import attribute_values
from ID3.model.utils import subset_for_attribute


def id3(dataset, remaining_attributes, target_attribute):
    classes = dataset[target_attribute]
    class_values = attribute_values(dataset, target_attribute)

    node = {}

    if len(class_values) == 1:
        node['label'] = class_values[0]
        return node

    if len(remaining_attributes) == 0:
        node['label'] = classes.mode()
        return node

    splitting_attribute = inf_gain(dataset, remaining_attributes, target_attribute)

    node['attribute'] = splitting_attribute
    node['nodes'] = {}

    splitting_attribute_values = attribute_values(dataset, splitting_attribute)

    remaining_attributes_for_subtrees = [attribute for attribute in remaining_attributes if attribute != splitting_attribute]

    for attribute_value in splitting_attribute_values:
        subset = subset_for_attribute(dataset, splitting_attribute, attribute_value)
        node['nodes'][attribute_value] = id3(subset, remaining_attributes_for_subtrees, target_attribute)

    return node
