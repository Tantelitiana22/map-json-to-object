import pkg_resources

from deserealization import ApplyMapping
from deserealization.usecase.map_json import Json


def get_json_to_object(json_file_path: str, model=Json()) -> Json:
    json_absolute_path_customers = pkg_resources.resource_filename(__name__, json_file_path)
    return ApplyMapping.get(path=json_absolute_path_customers, model=model)
