import pytest

from working import convert

def test_convert():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:32 AM to 5:59 PM") == "09:32 to 17:59"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"

    with pytest.raises(ValueError):
        convert("")
    with pytest.raises(ValueError):
        convert("13 AM to 4 PM")
    with pytest.raises(ValueError):
        convert("6 AM to 16 PM")
    with pytest.raises(ValueError):
        convert("Cat to dog")
    with pytest.raises(ValueError):
        convert("6:00 AM 2:00 PM")
    with pytest.raises(ValueError):
        convert("6:60 AM to 2:00 PM")
    with pytest.raises(ValueError):
        convert("6:00 AM 2:71 PM")
