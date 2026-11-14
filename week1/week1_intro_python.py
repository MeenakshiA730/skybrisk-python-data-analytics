"""Week 1: Introduction to Python Programming
Covers variables, data types, operators, input/output, if-else, for/while loops.
Run: python week1_intro_python.py
"""


# ---------- Hands-on 1: Temperature converter ----------
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9


def temperature_converter():
    print("\n--- Temperature Converter ---")
    try:
        value = float(input("Enter temperature value: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    unit = input("Is this in (C)elsius or (F)ahrenheit? ").strip().upper()
    if unit == "C":
        print(f"{value:.1f} C = {celsius_to_fahrenheit(value):.1f} F")
    elif unit == "F":
        print(f"{value:.1f} F = {fahrenheit_to_celsius(value):.1f} C")
    else:
        print("Unit must be C or F.")


# ---------- Hands-on 2: Calculator ----------
def calculator():
    print("\n--- Calculator ---")
    while True:  # while loop: repeat until user quits
        expr = input("Enter 'number operator number' (e.g. 8 * 3) or 'q' to quit: ").strip()
        if expr.lower() == "q":
            break
        parts = expr.split()
        if len(parts) != 3:
            print("Format: number operator number")
            continue
        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
        except ValueError:
            print("Operands must be numbers.")
            continue
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = "Error: division by zero" if b == 0 else a / b
        elif op == "**":
            result = a ** b
        elif op == "%":
            result = a % b if b != 0 else "Error: modulo by zero"
        else:
            result = "Unknown operator"
        print("Result:", result)


# ---------- Client project: average temperature ----------
def average_temperature_report():
    print("\n--- Client Project: Weekly Temperature Report ---")
    daily_temps = {
        "Mon": 28.5, "Tue": 30.1, "Wed": 29.4, "Thu": 31.8,
        "Fri": 27.9, "Sat": 26.5, "Sun": 28.0,
    }
    total = 0
    hottest_day, coolest_day = None, None
    for day, temp in daily_temps.items():  # for loop
        total += temp
        if hottest_day is None or temp > daily_temps[hottest_day]:
            hottest_day = day
        if coolest_day is None or temp < daily_temps[coolest_day]:
            coolest_day = day
    average = total / len(daily_temps)
    print(f"Average temperature : {average:.2f} C")
    print(f"Hottest day         : {hottest_day} ({daily_temps[hottest_day]} C)")
    print(f"Coolest day         : {coolest_day} ({daily_temps[coolest_day]} C)")
    print("Days above average  :", [d for d, t in daily_temps.items() if t > average])


if __name__ == "__main__":
    average_temperature_report()      # runs without input
    temperature_converter()
    calculator()
