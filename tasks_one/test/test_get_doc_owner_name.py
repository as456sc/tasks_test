from tasks_one.program import get_doc_owner_name
import pytest


@pytest.mark.parametrize(
        'number, expected_res',
        [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов"),
            ("10006", "Аристарх Павлов"),
            ("14685", None)
        ]
    )
    
def test_get_doc_owner_name(number, expected_res):
    actual_res = get_doc_owner_name(number)
    assert actual_res == expected_res