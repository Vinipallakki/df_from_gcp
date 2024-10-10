import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def log_message(message):
    """Log incoming Pub/Sub messages."""
    logging.info(f'Received message: {message}')
    return message

def parse_message(message):
    """Parse JSON message from Pub/Sub."""
    return json.loads(message)

def run():
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-etl-job',
        staging_location='gs://dataflow-staging-us-central1-627003217872/staging/',
        temp_location='gs://dataflow-staging-us-central1-627003217872/temp/',
        region='us-central1',
        streaming=True,
        runner='DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    # Read from Pub/Sub and process messages
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/real-time-subscription')
        | 'Log Messages' >> beam.Map(log_message)  # Log incoming messages
        | 'Parse JSON' >> beam.Map(parse_message)  # Parse JSON messages
    )

    # Write data directly to BigQuery
    lines | 'Write to BigQuery' >> WriteToBigQuery(
        table='banded-edge-437103-i9:my_realtime_dataset.realtime_table',  # Replace with your BigQuery project:dataset.table
        schema='name:STRING, age:INTEGER, salary:FLOAT',
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
