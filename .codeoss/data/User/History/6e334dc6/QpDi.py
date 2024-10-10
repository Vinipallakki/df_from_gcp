import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
# from apache_beam.transforms.window import FixedWindows, AccumulationMode
from apache_beam import triggers
import csv

def parse_csv(line):
    """Parse CSV line into a dictionary."""
    row = list(csv.reader([line]))[0]
    return {
        'name': row[0],
        'age': int(row[1]),  # Convert age to integer
        'salary': float(row[2])  # Convert salary to float
    }

def run():
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-etl-job',
        staging_location='gs://banded-edge-437103-i9/staging/',
        temp_location='gs://banded-edge-437103-i9/temp/',
        region='us-central1',
        runner='DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    # Read from Pub/Sub and apply windowing
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/topic_1-sub')  # Replace with your subscription ID
        | 'Parse CSV' >> beam.Map(parse_csv)
        | 'Window into fixed intervals' >> beam.WindowInto(
            FixedWindows(5),
            trigger=triggers.AfterProcessingTime(1),  # Trigger after 1 second
            # accumulation_mode=AccumulationMode.ACCUMULATING
        )
        | 'Format for BigQuery' >> beam.Map(lambda x: {
            'name': x['name'],
            'age': x['age'],
            'salary': x['salary']
        })
    )

    # Write transformed data to BigQuery
    lines | 'Write to BigQuery' >> WriteToBigQuery(
        table='banded-edge-437103-i9:first.second',  # Replace with your BigQuery project:dataset.table
        schema='name:STRING, age:INTEGER, salary:FLOAT',
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
