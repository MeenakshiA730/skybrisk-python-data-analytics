"""Week 2: Data Structures and Functions
Lists, tuples, dicts, sets, functions, lambda, recursion, list comprehension,
plus a data-cleaning client project.
Run: python week2_data_structures_functions.py
"""


# ---------- Hands-on: data structures ----------
def data_structure_demo():
    print("--- Data structures ---")
    nums = [4, 8, 15, 16, 23, 42]            # list: ordered, mutable
    point = (12.97, 77.59)                    # tuple: ordered, immutable
    unique = set([1, 2, 2, 3, 3, 3])          # set: unique values only
    student = {"name": "Asha", "score": 91}   # dict: key -> value
    print(nums, point, unique, student)


# ---------- Hands-on: functions ----------
def sum_of_squares(numbers):
    return sum(n ** 2 for n in numbers)


def factorial(n):                              # recursion
    return 1 if n <= 1 else n * factorial(n - 1)


def filter_above(numbers, threshold):
    return [n for n in numbers if n > threshold]   # list comprehension


square = lambda x: x ** 2                      # lambda function


def transformations_demo():
    print("\n--- Functions & transformations ---")
    data = [3, 7, 12, 5, 20, 9]
    print("Sum of squares     :", sum_of_squares(data))
    print("Factorial(5)       :", factorial(5))
    print("Filtered > 6       :", filter_above(data, 6))
    print("Squared (lambda)   :", list(map(square, data)))
    print("Evens (lambda)     :", list(filter(lambda x: x % 2 == 0, data)))
    print("Sorted by last digit:", sorted(data, key=lambda x: x % 10))


# ---------- Client project: data cleaning ----------
def clean_records(records):
    """Remove duplicates, drop incomplete rows, standardise text, filter by age."""
    seen = set()
    cleaned = []
    for r in records:
        if not r.get("name") or r.get("age") is None or not r.get("city"):
            continue                                   # drop missing values
        record = {
            "name": r["name"].strip().title(),
            "age": int(r["age"]),
            "city": r["city"].strip().title(),
        }
        key = (record["name"], record["city"])
        if key in seen:                                # drop duplicates
            continue
        seen.add(key)
        cleaned.append(record)
    return [r for r in cleaned if 18 <= r["age"] <= 65]   # filter valid ages


def data_cleaning_project():
    print("\n--- Client project: data cleaning ---")
    raw = [
        {"name": " asha ", "age": 25, "city": "bangalore"},
        {"name": "Asha", "age": 25, "city": "Bangalore"},   # duplicate
        {"name": "ravi", "age": None, "city": "kochi"},      # missing age
        {"name": "meera", "age": 17, "city": "chennai"},     # under 18
        {"name": "john", "age": 34, "city": " Mumbai "},
        {"name": "", "age": 40, "city": "delhi"},            # missing name
        {"name": "priya", "age": 29, "city": "kozhikode"},
    ]
    cleaned = clean_records(raw)
    print(f"Raw rows: {len(raw)} | Cleaned rows: {len(cleaned)}")
    for r in cleaned:
        print(r)
    print("Unique cities:", sorted({r["city"] for r in cleaned}))


if __name__ == "__main__":
    data_structure_demo()
    transformations_demo()
    data_cleaning_project()
