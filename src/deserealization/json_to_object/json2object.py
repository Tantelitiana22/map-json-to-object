import contextlib
import json
import copy
from typing import List


def deserialize(data, model)->List:
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
    if isinstance(data, list):
        models = []
        for d in data:
            obj = copy.copy(model)
            results = deserialize(d, obj)
            models.append(results)
        return models
    elif isinstance(data, dict):
        obj = copy.copy(model)
        for k, v in data.items():
            if not isinstance(v, dict) and not isinstance(v, list):
                setattr(obj, k, v)
            elif isinstance(v, list):
                with contextlib.suppress(Exception):
                    attr = getattr(obj, k)
                    result = deserialize(v, attr[0])
                    setattr(obj, k, result)
            else:
                with contextlib.suppress(Exception):
                    attr = getattr(obj, k)
                    result = deserialize(v, attr)
                    setattr(obj, k, result)
        return obj
    elif isinstance(data, str):
        return deserialize(json.loads(data), model)
    else:
        raise ValueError('Data representation of model needs to be in a list of dictionaries, dictionary or str json. '
                         'Check to see if format is correct.')
