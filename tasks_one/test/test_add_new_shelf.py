from tasks_one.program import add_new_shelf
import pytest
 

@pytest.mark.parametrize(
        'shelf, expected_res',
        [
            ('4', ('4', True)),
            ('5', ('5', True)),
            ('3', ('3', False))
        ]
    )
def test_add_new_shelf( shelf, expected_res):
    actual_res = add_new_shelf(shelf)
    assert actual_res == expected_res