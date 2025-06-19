import pandas as pd
import sqlite3

pd.set_option('display.min_rows', 100)
pd.set_option('display.max_rows', 100)

db_path = '../imdb.db'

def run_query(sql_path, db_path):
    with open(sql_path, 'r') as file:
        sql_query = file.read()

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query(sql_query, conn)

    conn.close()
    print(df)

"""
    Creates New Table of a title and it's genres
    Explodes the genres (splits the genres from an arrary/string with seperated
    by commas into multiple entries per genre).
    Goes from
        tconst | Adventure,Action,Western
    to
        tconst | Adventure
        tconst | Action
        tconst | Western
"""
def explode_genres(db_path):
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS title_genres (tconst TEXT NOT NULL, genre TEXT NOT NULL)')
    df = pd.read_sql_query("""
                        SELECT tconst, genres FROM title_basics WHERE genres IS NOT NULL AND genres != '\\N'
                        """, conn)
    df['genres'] = df['genres'].str.split(',')
    df_exploded = df.explode('genres')
    df_exploded = df_exploded.rename(columns={'genres': 'genre'})
    df_exploded.to_sql('title_genres', conn, if_exists='replace', index=False)

#run_query('../queries/top_directors.sql', db_path)

#Explode the genres before running the genre population over time query
#explode_genres(db_path)
#run_query('../queries/genre_pop_over_time.sql', db_path)

#run_query('../queries/most_prolific_actors.sql', db_path)

explode_genres(db_path)
run_query('../queries/average_runtime_by_genre.sql', db_path)
