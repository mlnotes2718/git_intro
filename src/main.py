# src/main.py  ← BUGGY VERSION

def calculate_bmi(weight_lb: float, height_m: float) -> float:
    """
    BUG: parameter says lb but we forget to convert lb → kg.
    The formula receives the wrong unit and silently produces a wrong answer.
    """
    bmi = weight_lb / (height_m ** 2)   # ← weight_lb used directly — WRONG
    return round(bmi, 2)


def bmi_category(bmi: float) -> str:
    if bmi < 18.5:   return "Underweight"
    elif bmi < 25.0: return "Normal weight"
    elif bmi < 30.0: return "Overweight"
    else:            return "Obese"


if __name__ == "__main__":
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in metres: "))
    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is {bmi} — {bmi_category(bmi)}")