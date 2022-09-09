from dataclasses import dataclass, field
from typing import List


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


@dataclass
class MappingWithRequiredField:
    type: str = field(default="")
    data_type: str = field(default="")
    source_field: str = field(default="")
    target_field: str = field(default="")
    action: str = field(default="", metadata=dict(required=False))


@dataclass
class EntityWithRequiredField:
    entity_name: str = field(default="")
    mappings: List[MappingWithRequiredField] = field(default_factory=lambda: [MappingWithRequiredField()])


@dataclass
class JsonWithRequiredField:
    source_name: str = field(default="")
    entities: List[EntityWithRequiredField] = field(default_factory=lambda: [EntityWithRequiredField()])
