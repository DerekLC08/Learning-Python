from plates import is_valid

def test_correct():
    assert is_valid("AAA222") == True
    assert is_valid("BB33") == True

def test_fzero():
    assert is_valid("DDD012") == False

def test_length():
    assert is_valid("ABCD123") == False
    assert is_valid("L") == False

def test_start():
    assert is_valid("12CD") == False
    assert is_valid("C4") == False

def test_middle():
    assert is_valid("AC3BD4") == False

def test_end():
    assert is_valid("AC90D") == False

def test_alphanumeric():
    assert is_valid("AC.,!2") == False

