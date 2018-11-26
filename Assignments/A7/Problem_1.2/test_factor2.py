import factor2

def test_factor2():
    assert factor2.smallest_factor(1) == 1, "failed on n=1"
    assert factor2.smallest_factor(2) == 2, "failed on n=2"
    assert factor2.smallest_factor(7) == 7, "failed on prime numbers"
    assert factor2.smallest_factor(9) == 3, "failed on number that's a square"
    assert factor2.smallest_factor(8) == 2, "failed on number with the smallest factor which is equal to its rounded-down square root"
