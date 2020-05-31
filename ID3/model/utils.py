def attribute_values(dataset, attribute):
    return dataset[attribute].unique()


def subset_for_attribute(dataset, splitting_attribute, attribute_value):
    return dataset.loc[dataset[splitting_attribute] == attribute_value]
