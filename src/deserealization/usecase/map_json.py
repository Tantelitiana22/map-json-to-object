import json
from dataclasses import dataclass, field
from typing import TypeVar, List

from deserealization.json_to_object.json2object import deserialize

T = TypeVar('T')

encoding = "utf-8"


@dataclass
class Mapping:
    type: str = field(default="")
    data_type: str = field(default="")
    source_field: str = field(default="")
    target_field: str = field(default="")
    action: str = field(default="")


@dataclass
class Entity:
    entity_name: str = field(default="")
    mappings: List[Mapping] = field(default_factory=lambda: [Mapping()])


@dataclass
class Json:
    source_name: str = field(default="")
    entities: List[Entity] = field(default_factory=lambda: [Entity()])


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
