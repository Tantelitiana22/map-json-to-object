from __future__ import annotations

import copy
import json
from typing import List, Dict, Optional
from dataclasses import is_dataclass, Field
from deserealization.typing import IDataClass


class Json2Object:
    """
    class how allow to convert json to defined object
    :data: is a dict or list or string to map
    :model: is the object model to use for deserialization
    """

    def __init__(self, data, model: IDataClass | str):
        if not data or isinstance(data, str) and not data.strip():
            raise ValueError('The data most not to be null or empty.')
        if not is_dataclass(model) and not isinstance(model, str):
            raise ValueError('The model most be a dataclass.')
        if isinstance(data, dict):
            self.model_and_data_validator(data, model)
        self.data = data
        self.model: IDataClass | str = model if isinstance(model, str) else copy.copy(model)

    @staticmethod
    def model_and_data_validator(data: Dict, model: IDataClass | str):
        if isinstance(model, str):
            return
        data_keys = list(data.keys())
        model_attributes = list(model.__dataclass_fields__.keys())
        if diff_field := list(set(model_attributes) - set(data_keys)):
            for field in diff_field:
                field_value: Optional[Field] = model.__dataclass_fields__.get(field)
                if _ := (field_value.metadata.get("required") in [None, True]) if field_value else False:
                    raise ValueError(f"Field not match. Some field are missing: {diff_field}. If this field is not "
                                     f"required, in dataclass field, add option metadata=dict(required=False).")

    def deserialize_list_data(self, data: List) -> List | IDataClass:
        """
        Parameters
        ----------
        data: data of type list
        Returns list of model
        -------
        """
        if isinstance(self.model, str):
            return data
        return [Json2Object(d, self.model).build() for d in data]

    def deserialize_dict_data(self, data: Dict) -> IDataClass | str | List:
        """
        Parameters
        ----------
        data: of type dict
        Returns model
        -------
        """
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                attr = getattr(self.model, key)
                sub_model = attr[-1] if isinstance(value, list) else attr
                result = Json2Object(value, sub_model).build()
            else:
                result = value
            setattr(self.model, key, result)
        return self.model

    def deserialize_str_data(self, data: str) -> List | IDataClass | str:
        """
        Parameters
        ----------
        data: if data is str convert to json object dict
        Returns
        -------
        """
        return Json2Object(json.loads(data), self.model).build()

    def build(self) -> List | IDataClass | str:
        """
        Returns a model or a list of model
        -------
        """
        if isinstance(self.data, list):
            return self.deserialize_list_data(self.data)
        if isinstance(self.data, dict):
            return self.deserialize_dict_data(self.data)
        if isinstance(self.data, str):
            return self.deserialize_str_data(self.data)
        raise ValueError("data most be dict or list or str deserializable")
