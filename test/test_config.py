import pytest

class NotInRange(Exception):
    def __init__(self,message = "Value not in range"):
        self.message = message
        super().__init__(self.message)

def test_generic():
    a = 10
    with pytest.raises(NotInRange):
        if a is not range(10,20):
            raise NotInRange


def test_something():
    a = 3
    b = 3
    assert a == b
