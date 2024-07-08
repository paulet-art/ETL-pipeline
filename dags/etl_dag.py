from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.extract import extract_data
from scripts.load import load_transformed_data

default_args = {
    'owner' : 'paulet',
    'depends_on_past' : False,
    'start_date' : datetime(2024, 7, 8),
    'retries' : 2,
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description="a sales etl pipeline dag",
    schedule='@daily'
)

def extract_task():
    api_data, csv_data = extract_data()
    return api_data, csv_data

def load_task(ti, **kwargs):
    load_data = ti.xcom_pull(task_ids='transform')
    load_transformed_data(load_data)

extract = PythonOperator(
    task_id = 'extract',
    python_callable = extract_task,
    dag=dag
)

load = PythonOperator(
    task_id='load',
    python_callable=load_task, 
    dag=dag
)

extract >> load