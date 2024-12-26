import json
import re
from os import system
from typing import Dict


def parse_principles(path) -> Dict:
    with open(path, 'r') as file:
        data = json.load(file)
        return data


class PParser:

    def __init__(self):
        self._mask = r'\(\s*([XY])\s*(.*?)\s*(\d|\w)*\s*,\s*([XY])\s*(.*?)\s*(\d|\w)*\s*\)'

    def try_parse_string(self, string) -> []:
        if not (match := re.search(self._mask, string)):
            return
        return match.groups()
