from typing import List
from dataclasses import dataclass, field
from deserealization.typing import IDataClass


@dataclass
class Mapping(IDataClass):
    type: str = field(default="")
    data_type: str = field(default="")
    source_field: str = field(default="")
    target_field: str = field(default="")
    action: str = field(default="")


@dataclass
class Entity(IDataClass):
    entity_name: str = field(default="")
    mappings: List[Mapping] = field(default_factory=lambda: [Mapping()])


@dataclass
class Json(IDataClass):
    source_name: str = field(default="")
    entities: List[Entity] = field(default_factory=lambda: [Entity()])


@dataclass
class MappingWithRequiredField(IDataClass):
    type: str = field(default="")
    data_type: str = field(default="")
    source_field: str = field(default="")
    target_field: str = field(default="")
    action: str = field(default="", metadata=dict(required=False))


@dataclass
class EntityWithRequiredField(IDataClass):
    entity_name: str = field(default="")
    mappings: List[MappingWithRequiredField] = field(default_factory=lambda: [MappingWithRequiredField()])


@dataclass
class JsonWithRequiredField(IDataClass):
    source_name: str = field(default="")
    entities: List[EntityWithRequiredField] = field(default_factory=lambda: [EntityWithRequiredField()])


@dataclass
class EntityWithListFiled(IDataClass):
    entity_name: str = field(default="")
    tags: List[str] = field(default_factory=lambda: [''])
    mappings: List[Mapping] = field(default_factory=lambda: [Mapping()])


@dataclass
class JsonWithEntityTagged(IDataClass):
    source_name: str = field(default="")
    entities: List[EntityWithListFiled] = field(default_factory=lambda: [EntityWithListFiled()])
