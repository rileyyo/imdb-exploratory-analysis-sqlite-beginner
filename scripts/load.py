import pandas as pd
import sqlite3
import os

if not os.path.exists('../imdb.db'):
    print("📁 Creating new SQLite database: imdb.db")
else:
    print("📂 Using existing database: imdb.db")

# Connect to sqlite database
conn = sqlite3.connect('../imdb.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS name_basics;')

def load_tsv_to_sqlite(tsv_path, table_name, db_path='../imdb.db'):
    df = pd.read_csv(tsv_path, sep='\t', na_values='\\N')
    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"✅ Loaded {table_name}")

load_tsv_to_sqlite('../data/name.basics.tsv', 'name_basics')
load_tsv_to_sqlite('../data/title.akas.tsv', 'title_akas')
load_tsv_to_sqlite('../data//title.basics.tsv', 'title_basics')
load_tsv_to_sqlite('../data/title.crew.tsv', 'title_crew')
load_tsv_to_sqlite('../data/title.episode.tsv', 'title_episode')
load_tsv_to_sqlite('../data/title.principals.tsv', 'title_principals')
load_tsv_to_sqlite('../data/title.ratings.tsv', 'title_ratings')
