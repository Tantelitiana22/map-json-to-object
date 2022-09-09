import pytest
from deserealization.main import get_json_to_object
from deserealization.usecase.map_json import JsonWithRequiredField


def test_use_case():
    # GIVEN
    path_test = '/rules/mapping/customer_example_file.json'
    # WHEN
    result = get_json_to_object(json_file_path=path_test)
    entities = result.entities[0]
    mapping = entities.mappings[0]
    # THEN
    assert entities.entity_name == "customers"
    assert result.source_name == "CUSTOMERS"
    assert mapping.type == "oneToOne"
    assert mapping.data_type == "string"
    assert mapping.source_field == "code_document"
    assert mapping.target_field == "reference"
    assert mapping.action == "filter"


def test_required_field_mission_in_json():
    # GIVEN : file with action missing in mappers
    path_test = '/rules/mapping/bad_example_file.json'
    # THEN
    with pytest.raises(ValueError):
        get_json_to_object(json_file_path=path_test)


def test_required_field_false_in_model():
    # GIVEN
    path_test = '/rules/mapping/bad_example_file.json'
    model = JsonWithRequiredField()
    # WHEN
    result = get_json_to_object(json_file_path=path_test, model=model)
    entities = result.entities[0]
    mapping = entities.mappings[1]
    # THEN
    assert entities.entity_name == "customers"
    assert result.source_name == "CUSTOMERS"
    assert mapping.type == "oneToOne"
    assert mapping.data_type == "string"
    assert mapping.source_field == "code_document"
    assert mapping.target_field == "reference"
    assert mapping.action == ""
