from um import count

def test_count():
    assert count("umbrella") == 0
    assert count("um") == 1
    assert count("UM") == 1
    assert count("umbra, um") == 1
    assert count("um, um") == 2
    assert count("um um") == 2
    assert count("rum") == 0