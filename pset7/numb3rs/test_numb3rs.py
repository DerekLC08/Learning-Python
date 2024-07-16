from numb3rs import validate

def test_validate():
    assert validate("cat.mouse.lion.0") == False
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True
    assert validate("99.99.99.99") == True
    assert validate("279.0.6.6") == False
    assert validate("66.-7.-63.99") == False
    assert validate("") == False
    assert validate("70.435.22.55") == False