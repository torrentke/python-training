

# Pytest esetén egy teszteset az egy függvény
# Egy teszteset mindig csak egy dolgot tesztel
# Egy teszteset neve konvenció szerint a test szóval kezdődik

#használni akarom a calculations MODULBÓL az absolute függvényt
from calculations import absolute


def test_absolute_with_postive():
    # BDD = Behaviour Driven Development
    # 3 részből áll: given-when-then
    # given
    input = 5
    # when
    result = absolute(input)
    #then
    expected = 5
    assert result == expected

def test_absolute_with_negative():
    assert absolute(-5) == 5

def test_absolute_with_zero():
    assert absolute(0) == 0