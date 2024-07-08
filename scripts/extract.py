import pandas as pd     #for file
import requests     #for api data

def extract_from_csv(file_path):
    df_csv = pd.read_csv(file_path, encoding='utf-8')
    return df_csv

def extract_from_api(url):
    response = requests.get(url)
    data = response
    df_api = pd.DataFrame(data)
    return df_api


def extract_data():
    file_path = "/home/paulet/Desktop/ETL pipeline/data/retail_sales_dataset.csv"
    csv_data = extract_from_csv(file_path)

    url = "https://fakestoreapi.com/products?limit=10"
    api_data = extract_from_api(url)

    return api_data, csv_data

