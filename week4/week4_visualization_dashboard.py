"""Week 4: Data Visualization with Matplotlib and Seaborn
Basic plots, heatmap, pairplot, and a multi-panel dashboard.
Run: python week4_visualization_dashboard.py   (needs numpy, pandas, matplotlib, seaborn)
Outputs: dashboard.png, pairplot.png
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")                 # save to file; works without a display
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")


def build_dataset(n=300, seed=7):
    rng = np.random.default_rng(seed)
    study_hours = rng.normal(5, 1.5, n).clip(0.5, 10)
    attendance = (60 + 4 * study_hours + rng.normal(0, 6, n)).clip(30, 100)
    sleep = rng.normal(7, 1, n).clip(4, 10)
    score = (20 + 6 * study_hours + 0.3 * attendance + 2 * sleep
             + rng.normal(0, 6, n)).clip(0, 100)
    group = rng.choice(["Group A", "Group B", "Group C"], n)
    return pd.DataFrame({"study_hours": study_hours, "attendance": attendance,
                         "sleep_hours": sleep, "score": score, "group": group})


def basic_plots(df):
    """Hands-on: Matplotlib basics."""
    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    ax[0].plot(df["score"].head(30).values, marker="o")
    ax[0].set(title="Line plot: first 30 scores", xlabel="Student", ylabel="Score")
    ax[1].bar(["A", "B", "C"], df.groupby("group")["score"].mean())
    ax[1].set(title="Bar: average score by group", ylabel="Score")
    fig.tight_layout()
    fig.savefig("basic_plots.png", dpi=120)
    plt.close(fig)


def dashboard(df):
    """Client project: dashboard showing feature relationships."""
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    fig.suptitle("Student Performance Dashboard", fontsize=16, fontweight="bold")

    sns.scatterplot(data=df, x="study_hours", y="score", hue="group",
                    alpha=0.7, ax=axes[0, 0])
    sns.regplot(data=df, x="study_hours", y="score", scatter=False,
                color="black", ax=axes[0, 0])
    axes[0, 0].set_title("Study hours vs score")

    sns.histplot(data=df, x="score", bins=20, kde=True, ax=axes[0, 1])
    axes[0, 1].set_title("Score distribution")

    sns.boxplot(data=df, x="group", y="score", ax=axes[1, 0])
    axes[1, 0].set_title("Score by group")

    corr = df.drop(columns="group").corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=axes[1, 1])
    axes[1, 1].set_title("Correlation heatmap")

    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig("dashboard.png", dpi=130)
    plt.close(fig)

    pp = sns.pairplot(df, hue="group", corner=True, plot_kws={"alpha": 0.6})
    pp.savefig("pairplot.png", dpi=100)
    plt.close("all")
    return corr


if __name__ == "__main__":
    data = build_dataset()
    basic_plots(data)
    corr = dashboard(data)
    print("Strongest correlation with score:")
    print(corr["score"].drop("score").sort_values(ascending=False).round(2))
    print("Saved: basic_plots.png, dashboard.png, pairplot.png")
