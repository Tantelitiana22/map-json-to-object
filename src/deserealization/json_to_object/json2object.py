import copy
import json
from typing import List, Dict, TypeVar, Union, NewType
from dataclasses import is_dataclass

T = TypeVar("T")
DataType = NewType("DataType", Union[str, List, Dict])


class Json2Object:
    """
    class how allow to convert json to defined object
    :data: is a dict or list or string to map
    :model: is the object model to use for deserialization
    """

    def __init__(self, data: DataType, model: T):
        if not data or isinstance(data, str) and not data.strip():
            raise ValueError('The data most not to be null or empty.')
        if not is_dataclass(model):
            raise ValueError('The model most be a dataclass.')

        self.data = data
        self.model = copy.copy(model)

    def deserialize_list_data(self, data: List) -> List[T]:
        """
        Parameters
        ----------
        data: data of type list
        Returns list of model
        -------
        """
        return [Json2Object(d, self.model).build() for d in data]

    def deserialize_dict_data(self, data: Dict) -> T:
        """
        Parameters
        ----------
        data: of type dict
        Returns model
        -------
        """
        data_keys = list(data.keys())
        model_attributes = list(self.model.__dataclass_fields__.keys())
        if diff_field := list(set(model_attributes) - set(data_keys)):
            for field in diff_field:
                if self.model.__dataclass_fields__.get(field).metadata.get("required") in [None, True]:
                    raise ValueError(f"Field not match. Some field are missing: {diff_field}. If this field is not "
                                     f"required, in dataclass field, add option metadata=dict(required=False).")
        for key, value in data.items():
            if isinstance(value, (dict, list)):
                attr = getattr(self.model, key)
                sub_model = attr[-1] if isinstance(value, list) else attr
                result = Json2Object(value, sub_model).build()
            else:
                result = value
            setattr(self.model, key, result)
        return self.model

    def deserialize_str_data(self, data: str) -> T:
        """
        Parameters
        ----------
        data: if data is str convert to json object dict
        Returns
        -------
        """
        return Json2Object(json.loads(data), self.model).build()

    def build(self) -> Union[List[T], T]:
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
