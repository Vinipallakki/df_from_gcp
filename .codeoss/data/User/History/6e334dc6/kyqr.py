import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam import window

def parse_pubsub_message(message):
    """Parse Pub/Sub message into a dictionary."""
    # Decode the message data and split by comma
    name, age, salary = message.decode('utf-8').split(',')
    return {
        'name': name,
        'age': int(age),  # Convert age to integer
        'salary': float(salary)  # Convert salary to float
    }

def run():
    # Define pipeline options for Dataflow
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-pubsub-to-bq',
        staging_location='gs://banded-edge-437103-i9/staging/',  # Replace with your GCS staging bucket
        temp_location='gs://banded-edge-437103-i9/temp/',  # Replace with your GCS temp bucket
        region='us-central1',  # Specify your GCP region
        runner='DataflowRunner'  # Use 'DataflowRunner' for cloud execution, 'DirectRunner' for local testing
    )

    # Initialize the Apache Beam pipeline
    p = beam.Pipeline(options=options)

    # Step 1: Read data from Pub/Sub
    messages = (
        p
        | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/banded-edge-437103-i9/topics/topic_1')  # Replace with your topic
        | 'Window into fixed intervals' >> beam.WindowInto(window.FixedWindows(60))  # Example: 60-second fixed window
    )

    # Step 2: Transform the data
    transformed_data = messages | 'Parse Pub/Sub messages' >> beam.Map(parse_pubsub_message)

    # Step 3: Write transformed data to BigQuery
    transformed_data | 'Write to BigQuery' >> WriteToBigQuery(
        table='banded-edge-437103-i9:first.second',  # Replace with your BigQuery project:dataset.table
        schema='name:STRING, age:INTEGER, salary:FLOAT',
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,  # Create table if it doesn't exist
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND  # Append to table if it exists
    )

    # Run the pipeline
    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
