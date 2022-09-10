import pytest
from deserealization.main import get_json_to_object, EnumJsonModel


def test_use_case():
    # GIVEN
    path_test = '/rules/mapping/customer_example_file.json'
    # WHEN
    result = get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json)
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
        get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json)


def test_required_field_false_in_model():
    # GIVEN
    path_test = '/rules/mapping/bad_example_file.json'
    # WHEN
    result = get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json_with_required_fields)
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


def test_use_case_with_list():
    # GIVEN
    path_test = '/rules/mapping/rules_with_list_of_string.json'
    # WHEN
    result = get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json_with_entity_tagged)
    entities = result.entities[0]
    # THEN
    assert entities.tags == ["sold", "delivery", 89]
    assert entities.code_numbers == [1924, 73829, 6977349]
    assert entities.three_last_prices == [8.99, 20.0, 12.44]


def test_bad_file_with_field_not_in_model():
    # GIVEN
    path_test = '/rules/mapping/bad_file_with_field_not_in_model.json'
    # THEN
    with pytest.raises(ValueError):
        get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json)


def test_skip_field_from_json_not_in_model():
    # GIVEN
    path_test = '/rules/mapping/bad_file_with_field_not_in_model.json'
    # WHEN
    result = get_json_to_object(json_file_path=path_test, model_enum=EnumJsonModel.json, skip_undefined_json_field=True)
    key_mappings = list(result.entities[0].mappings[0].__dict__.keys())
    # THEN
    assert "toto" not in key_mappings
