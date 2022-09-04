import pytest
from deserealization.main import get_json_to_object


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
