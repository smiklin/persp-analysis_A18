import months

def test_months():
    assert months.month_length("September", leap_year=False) == 30, "Failed on a 30 day month"
    assert months.month_length("January", leap_year=False) == 31, "Failed on a 31 day month"
    assert months.month_length("February", leap_year=False) == 28, "Failed on a non-leap February"
    assert months.month_length("February", leap_year=True) == 29, "Failed on a leap February"
