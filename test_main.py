from main import somar


def test_somar():
    assert somar(2, 3) == 5
    assert somar(0, 0) == 0
