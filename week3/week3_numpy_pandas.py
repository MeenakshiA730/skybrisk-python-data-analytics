"""Week 3: NumPy and Pandas for Data Manipulation
Arrays, broadcasting, DataFrames, indexing, groupby, and a clean-and-aggregate project.
Run: python week3_numpy_pandas.py   (needs numpy, pandas)
"""
import numpy as np
import pandas as pd


# ---------- Hands-on: NumPy ----------
def numpy_demo():
    print("--- NumPy ---")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print("Shape:", a.shape, "| Mean:", a.mean(), "| Column sums:", a.sum(axis=0))
    print("Broadcasting (a + [10,20,30]):\n", a + np.array([10, 20, 30]))
    print("Boolean mask (a > 3):", a[a > 3])


# ---------- Hands-on: Pandas basics ----------
def pandas_demo():
    print("\n--- Pandas basics ---")
    df = pd.DataFrame({"city": ["Kochi", "Kochi", "Mumbai", "Delhi"],
                       "sales": [120, 90, 200, 150]})
    s = df["sales"]                                 # Series
    print("Series mean:", s.mean())
    print("Row by label:\n", df.loc[0])
    print("Filtered:\n", df[df["sales"] > 100])
    print("Grouped:\n", df.groupby("city")["sales"].sum())


# ---------- Client project: clean and aggregate ----------
def build_sample_dataset(n=200, seed=42):
    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "region": rng.choice(["North", "South", "East", "West"], n),
        "product": rng.choice(["A", "B", "C"], n),
        "units": rng.integers(1, 50, n).astype(float),
        "unit_price": rng.normal(100, 15, n).round(2),
    })
    # inject messiness: missing values and duplicates
    df.loc[rng.choice(n, 12, replace=False), "units"] = np.nan
    df.loc[rng.choice(n, 8, replace=False), "unit_price"] = np.nan
    df = pd.concat([df, df.iloc[:5]], ignore_index=True)
    return df


def client_project():
    print("\n--- Client project: clean and aggregate ---")
    df = build_sample_dataset()
    print("Rows before cleaning:", len(df))
    print("Missing values:\n", df.isna().sum())

    df = df.drop_duplicates()
    df = df.dropna(subset=["units", "unit_price"])      # remove missing values
    df["revenue"] = df["units"] * df["unit_price"]
    print("Rows after cleaning :", len(df))

    print("\nAverage units & price overall:")
    print(df[["units", "unit_price"]].mean().round(2))

    summary = (df.groupby(["region", "product"])
                 .agg(avg_units=("units", "mean"),
                      avg_price=("unit_price", "mean"),
                      total_revenue=("revenue", "sum"))
                 .round(2))
    print("\nAggregated by region & product:\n", summary.head(8))

    df.to_csv("cleaned_sales.csv", index=False)
    print("\nSaved cleaned_sales.csv")


if __name__ == "__main__":
    numpy_demo()
    pandas_demo()
    client_project()
