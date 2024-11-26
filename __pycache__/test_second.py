import Target07 as s01

def test_cir_3():
    outcome = s01.circumference(3)
    
    assert outcome == 18.85

def test_cir_3p5():
    outcome = s01.circumference(3.5)
    
    assert outcome == 21.99

def test_cir_0():
    outcome = s01.circumference(0)

    assert outcome == 0.000

def test_cir_9p9():
    outcome = s01.circumference(9.9)

    assert outcome == 62.20

def test_cir_4p18():
    outcome = s01.circumference(4.18)

    assert outcome == 26.26

def test_cir_5p5():
    outcome = s01.circumference(5.5)

    assert outcome == 34.56


def test_digit_9p9():
    assert len(str(s01.circumference(9.9))) == 4

def test_digit_0():
    assert len(str(s01.circumference(0))) == 4

def test_digit_1():
    assert len(str(s01.circumference(1))) == 4

def test_digit_0p1():
    assert len(str(s01.circumference(0.1))) == 4