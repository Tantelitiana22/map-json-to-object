"""
This main file is dedicated for the use-case example.
"""

from __future__ import annotations
from typing import List
import pkg_resources

from deserealization import ApplyMapping
from deserealization.usecase.map_json import Json, JsonWithRequiredField


def get_json_to_object(json_file_path: str, model: Json | JsonWithRequiredField) -> List | Json | JsonWithRequiredField:
    json_absolute_path_customers = pkg_resources \
        .resource_filename(__name__, json_file_path)
    return ApplyMapping.get(path=json_absolute_path_customers, model=model)  # type: ignore
