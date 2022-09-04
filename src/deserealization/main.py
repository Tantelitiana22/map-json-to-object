import pkg_resources
from deserealization.usecase.map_json import Json, ApplyMapping


def get_json_to_object(json_file_path: str) -> Json:
    json_absolute_path_customers = pkg_resources.resource_filename(__name__, json_file_path)
    return ApplyMapping.get(path=json_absolute_path_customers, model=Json())
