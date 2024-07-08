import pandas as pd
import sqlite3
from extract import extract_data

def load_data(df, db_path, table_name):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

def load_transformed_data(api_data, csv_data):
    db_path = "data/database.db"
    table_name_api = "api_data"
    table_name_csv = "csv_data"

    load_data(api_data, db_path, table_name_api)
    load_data(csv_data, db_path, table_name_csv) 

if __name__ == "__main__":
    api_data, csv_data = extract_data()
    load_transformed_data(api_data, csv_data)