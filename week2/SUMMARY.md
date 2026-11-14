# Week 2: Data Structures and Functions
SkyBrisk Data Analytics Internship | Meenakshi A

## Concepts learned
- **List** (ordered, mutable), **tuple** (ordered, immutable), **set** (unique values), **dictionary** (key-value pairs).
- **Functions:** reusable blocks with parameters and return values.
- **Lambda functions:** short anonymous functions used with `map`, `filter` and `sorted(key=...)`.
- **Recursion:** a function that calls itself with a base case (factorial).
- **List comprehension:** concise filtering and transforming, e.g. `[n for n in data if n > 6]`.

## Hands-on
Sum of squares, threshold filtering, factorial, and `map`/`filter`/`sorted` transformations using lambdas.

## Client project
A `clean_records()` function that drops rows with missing fields, standardises text (strip and title case), removes duplicates using a `set` of keys, and filters invalid ages. Of 7 raw records, 3 valid ones remained.

## Key takeaway
Choosing the right data structure simplifies the logic (a set made deduplication trivial), and small single-purpose functions make cleaning steps easy to test.

**Run:** `python week2_data_structures_functions.py`
