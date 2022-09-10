"""
Mapping json file to an Object Method
"""
from __future__ import annotations

import json
from typing import List
from deserealization.json_to_object import json2object
from deserealization.json_to_object.json2object import UnionBasicType
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
    def transform_json_to_object(mapping_str: str, model: IDataClass, skip_undefined_json_field: bool) \
            -> List | IDataClass | UnionBasicType:
        return json2object.Json2Object(mapping_str, model, skip_undefined_json_field).build()

    @classmethod
    def get(cls, path: str, model: IDataClass, skip_undefined_json_field: bool) -> List | IDataClass | UnionBasicType:
        return cls.transform_json_to_object(cls.__read_json(path), model, skip_undefined_json_field)
