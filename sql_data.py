import pandas as pd
import sqlite3

def load_csv_to_sqlite(csv_file_path: str, db_file_path: str):
    """
    Load CSV data into a SQLite database.

    Args:
        csv_file_path (str): Full path to the CSV file.
        db_file_path (str): SQLite database file path.
    """
    df = pd.read_csv(csv_file_path)

    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Movies (
        Title TEXT,
        Type TEXT,
        Release_Year INTEGER,
        Genre TEXT,
        Director TEXT,
        Production_House TEXT,
        Lead_Actors TEXT,
        Language TEXT,
        Budget_Millions REAL,
        Box_Office_Millions REAL,
        OTT_Platform TEXT,
        Runtime_Minutes INTEGER,
        No_of_Episodes INTEGER,
        IMDb_Rating REAL,
        Audience_Score INTEGER,
        Critics_Score INTEGER,
        Awards_Nominations INTEGER,
        Awards_Won INTEGER,
        Social_Media_Mentions INTEGER,
        User_Reviews_Count INTEGER,
        Viewership_Hours_Million REAL
    )
    ''')

    df.to_sql('Movies', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

    print(f"Data loaded successfully into {db_file_path}")
