import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.transforms.window import FixedWindows
import csv

def parse_csv(line):
    """Parse the CSV line into a dictionary."""
    row = list(csv.reader([line]))[0]
    return {
        'name': row[0],
        'age': int(row[1]),  # Convert age to integer
        'salary': float(row[2])  # Convert salary to float
    }

def run():
    options = PipelineOptions(
        project='YOUR_GCP_PROJECT_ID',  # Replace with your GCP project ID
        job_name='realtime-dataflow-pipeline',
        staging_location='gs://YOUR_BUCKET_NAME/staging/',  # Replace with your GCS bucket
        temp_location='gs://YOUR_BUCKET_NAME/temp/',  # Replace with your GCS bucket
        region='us-central1',
        runner='DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    # Read from Pub/Sub and apply windowing
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/YOUR_GCP_PROJECT_ID/subscriptions/real-time-subscription')
        | 'Parse CSV' >> beam.Map(parse_csv)
        | 'Window into fixed intervals' >> beam.WindowInto(FixedWindows(5))  # 5-second window
        | 'Format for BigQuery' >> beam.Map(lambda x: {
            'name': x['name'],
            'age': x['age'],
            'salary': x['salary']
        })
    )

    # Write the processed data to BigQuery
    lines | 'Write to BigQuery' >> WriteToBigQuery(
        table='YOUR_GCP_PROJECT_ID:my_realtime_dataset.realtime_table',  # Replace with your BQ table
        schema='name:STRING, age:INTEGER, salary:FLOAT',
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
