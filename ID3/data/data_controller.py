import pandas as pd


class DataController:
    def __init__(self):
        self.dataset = pd.read_csv(r"mushrooms.csv", delimiter=',')

    def get_dataset(self):
        return self.dataset

    def get_remaining_attributes(self):
        return self.dataset.drop(columns="class").keys()
