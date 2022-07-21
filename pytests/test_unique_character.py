from unique_char import *
import pytest


@pytest.mark.parametrize("string, expected_result", [('abbbccdf', 3),
                                                     ('445dfgg', 3),
                                                     ('!!ghhtt', 1), ])
def test_number_of_unique_chars(string, expected_result):
    assert unique_chars(string) == expected_result


@pytest.mark.parametrize("expected_exception, string, actual_exception", [(TypeError, '', 3),
                                                                          (TypeError, '', 3.1)])
def test_type_error(expected_exception, string, actual_exception):
    with pytest.raises(expected_exception):
        type(string, actual_exception)


def test_cache():
    unique_chars.cache_clear()
    unique_chars('abbbccdf')
    unique_chars('abbbccdf')
    hits = list(unique_chars.cache_info())[0]
    assert hits == 1
