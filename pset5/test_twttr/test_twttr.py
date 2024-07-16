from twttr import shorten

def test_consonant():
    assert shorten("qwrtypsdfghjklzxcvbnm") == "qwrtypsdfghjklzxcvbnm"

def test_upper():
    assert shorten("AEIOU") == ""
    assert shorten("UOIEA") == ""

def test_lower():
    assert shorten("aeiou") == ""
    assert shorten("uoiea") == ""

def test_double():
    assert shorten("QIIOOT") == "QT"

def test_number():
    assert shorten("1a2e3i") == "123"

def test_nonalphanumeric():
    assert shorten("u.@%,a") == ".@%,"

def test_combined():
    assert shorten("qUworIte#A5") == "qwrt#5"


