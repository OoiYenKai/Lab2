import Lab2

def test_find_min_max():
    Lab2.display_main_menu()
    test_arr = [5, 67, 32]
    result = Lab2.calc_min_max_temperature(test_arr)
    assert (result == [5, 67])

def test_calc_average():
    test_arr = [5, 67, 32]
    result = Lab2.calc_average_temperature(test_arr)
    assert (result == 34.666666666666664)

def test_calc_median_temperature():
    test_arr = [5, 67, 32]
    result = Lab2.calc_median_temperature(test_arr)
    assert (result == 32)
