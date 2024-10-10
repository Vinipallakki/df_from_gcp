import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

def parse_json(json_string):
  return beam.Row(**json.loads(json_string))

def write_to_bq(data, banded-edge-437103-i9, first, temperature_table):
  client = bigquery.Client(project=project_id)
  table_ref = client.dataset(dataset_id).table(table_id)
  errors = client.load_table_from_dataframe(data, table_ref)
  if errors:
    print(f"Errors loading data: {errors}")

def run(argv=None):
  options = PipelineOptions(argv=argv)
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).project = 'your-project-id'
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).runner = 'DataflowRunner'
  options.view_as(beam.cloud.dataflow.options.DataflowPipelineOptions).temp_location = 'gs://your-bucket/temp'

  with beam.Pipeline(options=options) as p:
    # Read from Pub/Sub
    lines = p | 'Read from Pub/Sub' >> beam.io.ReadFromPubSub(topic='projects/your-project-id/topics/temperature_topic')

    # Parse JSON
    parsed_data = lines | 'Parse JSON' >> beam.Map(parse_json)

    # Write to BigQuery
    parsed_data | 'Write to BigQuery' >> beam.ParDo(write_to_bq, project_id='your-project-id', dataset_id='your_dataset', table_id='temperature_table')

if __name__ == '__main__':
  run()