"""
Mapping json file to an Object Method
"""
from __future__ import annotations

import json
from typing import  List
from deserealization.json_to_object import json2object
from deserealization.typing import IDataClass

ENCODING = "utf-8"


class ApplyMapping:

    @staticmethod
    def __read_json(path: str) -> str:
        """ Get string from file"""
        with open(path, encoding=ENCODING) as json_file:
            mapping_str = json.loads(json_file.read())
        return mapping_str

    @staticmethod
    def transform_json_to_object(mapping_str: str, model: IDataClass) -> List | IDataClass | str:
        return json2object.Json2Object(mapping_str, model).build()

    @classmethod
    def get(cls, path: str, model: IDataClass) -> List | IDataClass | str:
        return cls.transform_json_to_object(cls.__read_json(path), model)
