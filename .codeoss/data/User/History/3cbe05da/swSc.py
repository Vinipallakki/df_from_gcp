from airflow import DAG
from airflow.providers.google.cloud.operators.dataproc import DataprocSubmitJobOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.utils.dates import days_ago
from airflow.operators.dummy_operator import DummyOperator

# Default arguments for the DAG
default_args = {
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
}

# Define the DAG
with DAG(
    'etl_dataproc_to_bq',
    default_args=default_args,
    schedule_interval='@daily',  # Run daily
    catchup=False,
) as dag:
    
    # Dummy task to mark the start
    start = DummyOperator(task_id='start')
    
    # Task 1: Submit Dataproc job
    dataproc_job = {
        'reference': {'project_id': 'banded-edge-437103-i9'},
        'placement': {'cluster_name': 'data-processing-cluster'},
        'pyspark_job': {'main_python_file_uri': 'gs://your-bucket-name/spark_jobs/spark_job.py'},
    }
    submit_dataproc_job = DataprocSubmitJobOperator(
        task_id='submit_dataproc_job',
        job=dataproc_job,
        location='your-region'
    )
    
    # Task 2: Load processed data from GCS to BigQuery
    load_to_bq = GCSToBigQueryOperator(
        task_id='load_to_bigquery',
        bucket='your-bucket-name',
        source_objects=['processed_data/processed_output.csv'],
        destination_project_dataset_table='your-project.your_dataset.your_table',
        source_format='CSV',
        skip_leading_rows=1,
        write_disposition='WRITE_TRUNCATE',
    )
    
    # Define task dependencies
    start >> submit_dataproc_job >> load_to_bq

