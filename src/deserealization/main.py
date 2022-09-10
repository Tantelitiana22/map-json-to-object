"""
This main file is dedicated for the use-case example.
"""

from __future__ import annotations

import enum
from typing import List, Union
import pkg_resources

from deserealization import ApplyMapping
from deserealization.usecase.map_json import Json, JsonWithRequiredField, JsonWithEntityTagged

UnionType = Union[JsonWithEntityTagged, Json, JsonWithRequiredField]


class EnumJsonModel(enum.Enum):
    json = Json
    json_with_required_fields = JsonWithRequiredField
    json_with_entity_tagged = JsonWithEntityTagged


def get_json_to_object(json_file_path: str, model_enum: EnumJsonModel) -> \
        List | UnionType:
    json_absolute_path_customers = pkg_resources \
        .resource_filename(__name__, json_file_path)
    return ApplyMapping.get(path=json_absolute_path_customers, model=model_enum.value())  # type: ignore
