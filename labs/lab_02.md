# Lab 2

## Objectives

Students:

- refresh their memories on working with Jupyter and pandas
- get practice with pagination and [concatenation](https://pandas.pydata.org/docs/user_guide/merging.html#concat) of datasets

## Steps

We'll be doing this lab as pair programming, with the TA floating around to help.

### Full class together

1. Go over [pair programming](../docs/pairing.md).
1. Talk through the steps below.
1. Set up groups with different people than the [project teams](../people/README.md).

### In groups

Students can look back at the [Computing in Context slides](https://computing-in-context.afeld.me/#schedule) if needed.

1. One person in each group, create a new notebook in [Google Colab](https://colab.research.google.com/).
   1. Add everyone's name.
   1. Share it with your teammate(s).
1. [Pick a dataset.](https://python-public-policy.afeld.me/en/columbia/assignments/open_ended.html)
   - Don't spend too long on this step, it's just for this lab.
1. Download the data as CSV/Excel.
1. Upload the file to Colab.
1. Load the data with pandas.
1. Confirm how many records have been loaded.
1. Compute an aggregate statistic (mean, median, sum, whatever).
1. Create a visualization.
   - Keep it simple.
1. Expand the dataset via pagination.
   - Start small in terms of page size and number of pages to be able to iterate quickly.
   - Don't need to get _all_ records necessarily; maybe cut it off at five pages worth.
1. Do the aggregate statistic and visualization using the expanded dataset and note how they've changed.
1. Turn in the notebook.
