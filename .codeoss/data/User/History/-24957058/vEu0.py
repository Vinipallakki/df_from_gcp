import json
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, SetupOptions, GoogleCloudOptions
from google.cloud import bigquery

# Function to parse JSON strings into dictionary objects
def parse_json(json_string):
    return beam.Row(**json.loads(json_string))

# Function to write DataFrame to BigQuery
def write_to_bq(data):
    client = bigquery.Client()  # Initialize BigQuery client
    dataset_ref = client.dataset('first')  # Reference to dataset
    table_ref = dataset_ref.table('temperature_table')  # Reference to table
    df = data.to_dataframe()  # Assuming 'data' is a PCollection of Rows
    errors = client.load_table_from_dataframe(df, table_ref).result()  # Load data to BigQuery
    if errors:
        print(f"Errors loading data: {errors}")

def run(argv=None):
    options = PipelineOptions(argv=argv)
    # Configure Dataflow options
    dataflow_options = options.view_as(GoogleCloudOptions)
    dataflow_options.project = 'banded-edge-437103-i9'
    dataflow_options.runner = 'DataflowRunner'  # Use 'DirectRunner' for local testing
    dataflow_options.temp_location = 'gs://banded-edge-437103-i9/temp'

    with beam.Pipeline(options=options) as p:
        # Read from Pub/Sub
        lines = (p 
                 | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/banded-edge-437103-i9/topics/temperature_topic'))

        # Parse JSON
        parsed_data = (lines 
                       | 'Parse JSON' >> beam.Map(parse_json))

        # Write to BigQuery
        (parsed_data 
         | 'Write to BigQuery' >> beam.Map(write_to_bq))

if __name__ == '__main__':
    run()
