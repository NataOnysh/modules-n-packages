# F = 9/5 * C + 32
def celsius_to_fahrenheit(temp: int) -> str:
    temp = (9/5) * temp + 32
    return f"{temp}°F"


# C=5/9(F−32)
def fahrenheit_to_celsius(temp: int) -> str:
    temp = (5/9) * (temp - 32)
    return f"{temp}°C"
