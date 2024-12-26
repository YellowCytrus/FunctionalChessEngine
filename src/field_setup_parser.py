import json


def parse_setup(path):
    with open(path, 'r') as file:
        data = json.load(file)
        return data

class FieldSetupParser:

    def __init__(self):
        pass


