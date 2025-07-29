import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch, helpers
import time

default_args= {
    'owner': 'Sesilia',
    'start_date': datetime(2024, 6, 7)
}

with DAG(
    'P2M3_Sesilia_Virdha_DAG',
    description='from csv to postgres',
    schedule_interval='10-30 9 * * 6',
    default_args=default_args,
    catchup=False
) as dag:
        start = EmptyOperator(task_id='start')
        end = EmptyOperator(task_id='end')

        @task()
        def extract():
            database = 'airflow'
            username = 'airflow'
            password = 'airflow'
            host = 'postgres'

            postgres_url = f'postgresql+psycopg2://{username}:{password}@{host}/{database}'

            engine = create_engine(postgres_url)
            conn = engine.connect()

            df = pd.read_sql_query('select * from table_m3', conn)

            df = pd.read_csv('/opt/airflow/data/P2M3_Sesilia_Virdha_data_raw.csv')
            print('Success extract to airflow')

        @task()
        def cleaning():
            '''
            Function used to transform data
            '''
            df = pd.read_csv('/opt/airflow/data/P2M3_Sesilia_Virdha_data_raw.csv')

            # Remove Duplicates (tidak ada)
            df.drop_duplicates(inplace=True)

            # Handle missing values
            df.fillna(df.mean(numeric_only=True), inplace=True)
            df.fillna(df.mode().iloc[0], inplace=True)

            # Normalisasi nama kolom
            df.columns = df.columns.str.strip()
            df.columns = df.columns.str.lower().str.replace(' ', '_').str.replace(r'[^0-9a-zA-Z_]', '', regex=True)

            df.to_csv('/opt/airflow/data/P2M3_Sesilia_Virdha_data_clean.csv', index=False)

        @task
        def loading():
            '''
            Function to load data to ElasticSearch
            '''
            time.sleep(10)  # beri waktu agar ES siap menerima koneksi

        try:
            es = Elasticsearch(
                "http://elasticsearch:9200",
                timeout=60,
                max_retries=5,
                retry_on_timeout=True
            )

            # Hapus index lama jika sudah ada
            if es.indices.exists(index="m3_sesil"):
                es.indices.delete(index="m3_sesil")
                print("Index lama dihapus")

            # Baca data dan kirim ulang
            df = pd.read_csv('/opt/airflow/data/P2M3_Sesilia_Virdha_data_clean.csv')
            df = df.fillna('')
            print(f"Jumlah record yang akan dikirim: {len(df)}")

            records = df.to_dict(orient='records')
            actions = [
                {
                    "_index": "m3_sesil",
                    "_source": record
                }
                for record in records
            ]

            helpers.bulk(es, actions, chunk_size=250)
            print("Data berhasil dikirim ke Elasticsearch")

        except Exception as e:
            print(f"Gagal mengirim data ke Elasticsearch: {e}")
            raise e

        start >> extract() >> cleaning() >> loading() >> end
