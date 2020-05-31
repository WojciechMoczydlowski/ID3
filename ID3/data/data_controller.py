import pandas as pd


class DataController:
    def __init__(self):
        self.dataset = pd.read_csv(r"mushrooms.csv", delimiter=',')

    def get_target_array(self):
        return self.dataset['class']

    def get_target_array(self):
        return self.dataset['class']