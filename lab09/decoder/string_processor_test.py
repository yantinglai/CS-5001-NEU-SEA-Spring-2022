from types import NoneType
from string_processor import StringProcessor


def test_process_string():
    sp = StringProcessor()
    assert sp.process_string("ab") == ""
    assert sp.process_string("ab*") == "b"
    assert sp.process_string("ab^") == "ba"
    assert sp.process_string("^") == ""
