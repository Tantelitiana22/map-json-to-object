import contextlib
import copy
import json
from typing import List


def deserialize(data, model) -> List:
    """
    Parameters
    ----------
    data : list of dictionaries of json model, dictionary or json string.
    model : The model that represents the data or empty class.

    Raises
    ------
    Exception
        Standard exception when incorrect data is passed.

    Returns
    -------
    Returns a single model of the passed in type or a list of models of the passed in type.

    """
    if not data or isinstance(data, str) and not data.strip():
        raise ValueError('The data passed in is either null or empty.')
    if not model or isinstance(model, str):
        raise ValueError('The model passed in is null or a string.')
    obj = copy.copy(model)
    if isinstance(data, list):
        return [deserialize(d, obj) for d in data]
    if isinstance(data, dict):
        for k, v in data.items():
            with contextlib.suppress(Exception):
                if isinstance(v, (dict, list)):
                    attr = getattr(obj, k)
                    model = attr[0] if isinstance(v, list) else attr
                    result = deserialize(v, model)
                else:
                    result = v
                setattr(obj, k, result)
        return obj
    if isinstance(data, str):
        return deserialize(json.loads(data), model)
    raise ValueError('Data representation of model needs to be in a list of dictionaries, dictionary or str json. '
                     'Check to see if format is correct.')
