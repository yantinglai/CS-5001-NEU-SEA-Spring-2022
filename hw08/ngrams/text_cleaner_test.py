"""Text cleaner test file"""
from text_cleaner import TextCleaner


def test_read_file():
    """test the text cleaner"""
    a = TextCleaner("corpse_bride.txt")
    s1 = "()test"
    s2 = "test, and\n"
    assert a.read_file(s1)[0] == "test"
    assert a.read_file(s2)[0] == "test COMMA and"
