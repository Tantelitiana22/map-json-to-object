"""
Mapping json file to an Object Method
"""

import json
from typing import TypeVar

from deserealization.json_to_object import json2object

ENCODING = "utf-8"
T = TypeVar('T')


class ApplyMapping:

    @staticmethod
    def __read_json(path: str) -> str:
        """ Get string from file"""
        with open(path, encoding=ENCODING) as json_file:
            mapping_str = json.loads(json_file.read())
        return mapping_str

    @staticmethod
    def transform_json_to_object(mapping_str: str, model: T) -> T:
        return json2object.Json2Object(mapping_str, model).build()

    @classmethod
    def get(cls, path: str, model: T) -> T:
        return cls.transform_json_to_object(cls.__read_json(path), model)
