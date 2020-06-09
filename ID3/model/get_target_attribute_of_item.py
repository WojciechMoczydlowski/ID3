# author: Jan Piotrowski, Wojciech Moczydlowski
def get_target_attribute_of_item(item, root):
    if 'label' in root:
        return root['label']
    else:
        root_attribute = root['attribute']
        value_of_attribute_in_item = item[root_attribute]
        if value_of_attribute_in_item in root['nodes']:
            node = root['nodes'][value_of_attribute_in_item]
            return get_target_attribute_of_item(item, node)
        else:
            get_target_attribute_of_item_with_unknowing_value(item, root)


def get_target_attribute_of_item_with_unknowing_value(item, root):
    def curry_get_target_attribute_from_node(curry_root):
        return get_target_attribute_of_item(item, curry_root)

    results = []
    for key in root['nodes'].keys():
        results.append(curry_get_target_attribute_from_node(root['nodes'][key]))
    return max(set(results), key=results.count)  # one line formula for getting most frequency element


def check_if_target_attribute_prediction_is_properly(item, target, root):
    return item[target] == get_target_attribute_of_item(item, root)
