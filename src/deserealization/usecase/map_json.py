import json
from typing import TypeVar, List

from deserealization.json_to_object.json2object import deserialize

T = TypeVar('T')

encoding = "utf-8"


class Mapping:
    type: str
    data_type: str
    source_field: str
    target_field: str
    action: str

    def __init__(self, types="",
                 data_type="",
                 source_field="",
                 target_field="",
                 action=""):  # NOSONAR
        self.type = types
        self.data_type = data_type
        self.source_field = source_field
        self.target_field = target_field
        self.action = action

    def __repr__(self):
        return ';'.join([self.type, self.data_type, self.source_field, self.target_field, self.action])

    def __str__(self):
        return self.__repr__()


class Entity:
    entity_name: str
    mappings = [Mapping()]


class Json:
    source_name: str
    entities: List[Entity] = [Entity()]


class ApplyMapping:

    @staticmethod
    def __read_json(path: str) -> str:
        """ Get string from file"""
        with open(path, encoding=encoding) as json_file:
            mapping_str = json.loads(json_file.read())
        return mapping_str

    @staticmethod
    def __transform_json_to_object(mapping_str: str, model: T) -> T:
        return deserialize(mapping_str, model)

    @classmethod
    def get(cls, path: str, model: T) -> T:
        return cls.__transform_json_to_object(cls.__read_json(path), model)
