import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from google.cloud import bigquery

def parse_json(json_string):
  return beam.Row(**json.loads(json_string))

def write_to_bq(data, project_id):
  client = bigquery.Client(project=project_id)
  dataset_ref = client.dataset('first')
  table_ref = dataset_ref.table('temperature_table')
  errors = client.load_table_from_dataframe(data, table_ref)
  if errors:
    print(f"Errors loading data: {errors}")

def run(argv=None):
  options = PipelineOptions(argv=argv)
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).project = 'banded-edge-437103-i9'
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).runner = 'DataflowRunner'
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).temp_location = 'gs://banded-edge-437103-i9/temp'

  with beam.Pipeline(options=options) as p:
    # Read from Pub/Sub
    lines = p | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/banded-edge-437103-i9/topics/temperature_topic')

    # Parse JSON
    parsed_data = lines | 'Parse JSON' >> beam.Map(parse_json)

    # Write to BigQuery
    parsed_data | 'Write to BigQuery' >> beam.ParDo(write_to_bq, project_id='banded-edge-437103-i9')

if __name__ == '__main__':
  run()