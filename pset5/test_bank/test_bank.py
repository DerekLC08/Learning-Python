from bank import value

def test_hello():
    assert value("hello") == 0

def test_hletter():
    assert value("hey") == 20

def test_uncommon():
    assert value("mornin'") == 100
    assert value("83110") == 100

def test_capital():
    assert value("Hello") == 0
    assert value("HI") == 20
    assert value("ohaiyO") == 100

def test_sentence():
    assert value("hello, how are you?") == 0
    assert value("hi! Now show me the cash.") == 20
    assert value("THIS IS A ROBBERY!") == 100
