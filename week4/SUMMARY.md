# Week 4: Data Visualization with Matplotlib and Seaborn
SkyBrisk Data Analytics Internship | Meenakshi A

## Concepts learned
- **Matplotlib:** figures and axes, line, bar, scatter and histogram plots, titles, labels and layout.
- **Seaborn:** statistical plots built on Matplotlib: `scatterplot` with `hue`, `histplot` with KDE, `boxplot`, `heatmap` for correlation matrices, and `pairplot` for pairwise relationships.
- Choosing the chart to fit the question: relationships (scatter), distributions (histogram, box), correlations (heatmap).

## Hands-on
Line and bar charts (`basic_plots.png`) and visualizations for dataset analysis.

## Client project
A four-panel dashboard (`dashboard.png`) on student performance features (study hours, attendance, sleep, score): scatter with trend line, score distribution, box plot by group, and a correlation heatmap, plus `pairplot.png`. Study hours (r = 0.83) and attendance (r = 0.72) correlated most strongly with score; sleep hours barely at all.

## Key takeaway
Visuals reveal relationships and outliers that summary statistics hide. The dashboard shows association, not causation.

**Run:** `python week4_visualization_dashboard.py` (requires `numpy`, `pandas`, `matplotlib`, `seaborn`)
