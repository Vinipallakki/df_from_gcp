import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.transforms.window import FixedWindows
from apache_beam.transforms.trigger import AfterProcessingTime, AccumulationMode, Repeatedly

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

    # Read from Pub/Sub and apply windowing with a custom trigger
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/real-time-subscription')  # Replace with your subscription ID
        | 'Window into fixed intervals' >> beam.WindowInto(
            FixedWindows(5),  # Use a fixed window of 5 seconds
            trigger=Repeatedly(AfterProcessingTime(10)),  # Trigger every 10 seconds of processing time
            accumulation_mode=AccumulationMode.DISCARDING  # Discard elements after they are triggered
        )
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
