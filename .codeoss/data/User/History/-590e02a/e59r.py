import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery


def parse_csv(line):
    """Parse CSV line into a dictionary."""
    import csv
    row = list(csv.reader([line]))[0]
    return {
        'name': row[0],
        'age': int(row[1]),  # Convert age to integer
        'salary': float(row[2])  # Convert salary to float
    }


def filter_header(indexed_row):
    """Filter out the header row (first row)."""
    index, row = indexed_row
    if index == 0:  # Skip the header row
        return False
    return True


def run():
    # Define pipeline options for Dataflow
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-etl-job',
        staging_location='gs://banded-edge-437103-i9/staging/',  # Replace with your GCS staging bucket
        temp_location='gs://banded-edge-437103-i9/temp/',  # Replace with your GCS temp bucket
        region='us-central1',  # Specify your GCP region
        runner='DataflowRunner'  # Use 'DataflowRunner' for cloud execution, 'DirectRunner' for local testing
    )

    # Initialize the Apache Beam pipeline
    p = beam.Pipeline(options=options)

    # Step 3: Read data from GCS
    lines = p | 'Read from GCS' >> beam.io.ReadFromText('gs://banded-edge-437103-i9/sample_data.csv')

    # Step 4: Add index to rows and filter out the header
    non_header_lines = (
        lines
        | 'Add Index' >> beam.transforms.util.WithKeys(lambda x: 0)  # Add index to each row
        | 'Filter Header' >> beam.Filter(filter_header)  # Remove the header row (index 0)
        | 'Remove Index' >> beam.Map(lambda indexed_row: indexed_row[1])  # Remove the index after filtering
    )

    # Step 5: Transform the data
    transformed_data = non_header_lines | 'Parse CSV' >> beam.Map(parse_csv)

    # Step 6: Write transformed data to BigQuery
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
