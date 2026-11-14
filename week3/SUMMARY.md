# Week 3: NumPy and Pandas for Data Manipulation
SkyBrisk Data Analytics Internship | Meenakshi A

## Concepts learned
- **NumPy arrays:** fast, typed, multi-dimensional data; vectorised operations replace Python loops.
- **Broadcasting:** arithmetic between arrays of different shapes.
- **Pandas Series and DataFrame:** labelled 1-D and 2-D data structures.
- **Indexing:** `.loc` (label-based), `.iloc` (position-based), and boolean filtering.
- **Grouping:** `groupby` with `agg` to summarise by category.

## Hands-on
Array statistics, masking and broadcasting in NumPy, and filtering and grouping in Pandas.

## Client project
Generated a 205-row sales dataset with injected missing values and duplicates. Removed duplicates and nulls (180 clean rows), computed revenue, calculated average units and price (25.91 units, 100.14 price), aggregated by region and product, and exported `cleaned_sales.csv`.

## Key takeaway
Inspect missing values and duplicates before aggregating, because they silently skew averages and totals.

**Run:** `python week3_numpy_pandas.py` (requires `numpy`, `pandas`)
