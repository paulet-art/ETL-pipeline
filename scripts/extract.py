import pandas as pd     #for file
import requests     #for api data
import psycopg2    #for db data

def extract_from_csv(file_path):
    df_csv = pd.read_csv(file_path)
    return df_csv

def extract_from_api(url):
    response = requests.get(url)
    data = response.json()
    df_api = pd.DataFrame(data)
    return df_api


def extract_data():
    file_path = "data/retail_sales_dataset.csv"
    csv_data = extract_from_csv(file_path)

    url = "https://fakestoreapi.com/products?limit=10"
    api_data = extract_from_api(url)

if __name__ == "__main__":
    extract_data()