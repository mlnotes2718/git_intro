from main import calculate_bmi, bmi_category

def test_normal_bmi():
    assert calculate_bmi(70, 1.75) == 22.86

def test_category_normal():
    assert bmi_category(22.86) == "Normal weight"