# 🎬 IMDb Data Exploration Project

This project explores real-world movie data from IMDb using Python, SQLite, and Jupyter Notebooks.
Wanted an introduction to data loading (tsv's to sqlite db using python), some manipulation (exploding movie genre column, creating new table), querying, and Jupyter Notebooks.
Mainly not for any use, but to document my learning progress. Can see the end goal of certain queries and plotting in the notebooks folder.

## ✅ Goals
- Practice loading TSV files into SQLite
- Run SQL queries on a multi-table schema
- Visualize trends in movie ratings and genres
- Uses sqlite's auto indexing for queries, could use parallelization platforms to speed up queries

## 📎 Files
- `load_data.py` – TSV to SQLite loader
- `notebooks/imdb_analysis.ipynb` – Analysis and visualizations
- `queries/` – SQL-only versions of key queries

## Data Setup

Due to size limits, the full IMDb datasets are not included in this repository.

To download the full dataset:

1. Visit [IMDb Datasets](https://developer.imdb.com/non-commercial-datasets/)
2. Download the files (e.g., `title.basics.tsv.gz`, `title.akas.tsv.gz`)
3. Place them in the `data/` directory
4. Run `scripts/load_data.py` to load into SQLite
