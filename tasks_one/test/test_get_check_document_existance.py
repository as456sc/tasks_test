from tasks_one.program import check_document_existance
import pytest


@pytest.mark.parametrize(
        'number, expected_res_one',
        [
            ("2207 876234", True),
            ("11-2", True),
            ("10006", True),
            ("19906", False)
        ]
    )
def test_check_document_existance(number, expected_res_one):
    actual_res = check_document_existance(number)
    assert actual_res == expected_res_one