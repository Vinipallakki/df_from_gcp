import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery

def run():
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-etl-job',
        staging_location='gs://hello_hi_9665/staging',
        temp_location='gs://hello_hi_9665/temp',
        region='us-central1',
        template_location='gs://hello_hi_9665/templete',
        streaming =True,  #added code to remove the grouby key error
        runner= 'DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    # Read from Pub/Sub without windowing
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/topic_1-sub')  # Replace with your subscription ID
    )

    # Write data directly to BigQuery
    lines | 'Write to BigQuery' >> WriteToBigQuery(
        table='banded-edge-437103-i9:my_realtime_dataset.realtime_table',  # Replace with your BigQuery project:dataset.table
        schema='name:STRING,
        create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
        write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
    )

    p.run().wait_until_finish()

if __name__ == '__main__':
    run()
