import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery

def run():
    options = PipelineOptions(
        project='banded-edge-437103-i9',  # Replace with your GCP project ID
        job_name='dataflow-etl-job',
        staging_location='gs://  File "/usr/lib/python3.12/contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/bucket.py", line 1088, in reload
    super(Bucket, self).reload(
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/_helpers.py", line 300, in reload
    api_response = client._get_resource(
                   ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/client.py", line 464, in _get_resource
    return self._connection.api_request(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/_http.py", line 90, in api_request
    return call()
           ^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/api_core/retry/retry_unary.py", line 293, in retry_wrapped_func
    return retry_target(
           ^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/api_core/retry/retry_unary.py", line 153, in retry_target
    _retry_error_helper(
  File "/usr/local/lib/python3.12/dist-packages/google/api_core/retry/retry_base.py", line 212, in _retry_error_helper
    raise final_exc from source_exc
  File "/usr/local/lib/python3.12/dist-packages/google/api_core/retry/retry_unary.py", line 144, in retry_target
    result = target()
             ^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/_http/__init__.py", line 482, in api_request
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/_http/__init__.py", line 341, in _make_request
    return self._do_request(
           ^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/_http/__init__.py", line 379, in _do_request
    return self.http.request(
           ^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/auth/transport/requests.py", line 534, in request
    self.credentials.before_request(auth_request, method, url, request_headers)
  File "/usr/local/lib/python3.12/dist-packages/google/auth/credentials.py", line 228, in before_request
    self._blocking_refresh(request)
  File "/usr/local/lib/python3.12/dist-packages/google/auth/credentials.py", line 191, in _blocking_refresh
    self.refresh(request)
  File "/usr/local/lib/python3.12/dist-packages/google/auth/compute_engine/credentials.py", line 126, in refresh
    self._retrieve_info(request)
  File "/usr/local/lib/python3.12/dist-packages/google/auth/compute_engine/credentials.py", line 103, in _retrieve_info
    self._service_account_email = info["email"]
                                  ~~~~^^^^^^^^^

WARNING:apache_beam.utils.retry:Retry with exponential backoff: waiting for 18.93080121563495 seconds before retrying _uncached_gcs_file_copy because we caught exception: TypeError: string indices must be integers, not 'str'
 Traceback for above exception (most recent call last):
  File "/home/youwantsomethings/.local/lib/python3.12/site-packages/apache_beam/utils/retry.py", line 298, in wrapper
    return fun(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^
  File "/home/youwantsomethings/.local/lib/python3.12/site-packages/apache_beam/runners/dataflow/internal/apiclient.py", line 566, in _uncached_gcs_file_copy
    self.stage_file(to_folder, to_name, f, total_size=total_size)
  File "/home/youwantsomethings/.local/lib/python3.12/site-packages/apache_beam/runners/dataflow/internal/apiclient.py", line 671, in stage_file
    bucket = self._storage_client.get_bucket(bucket_name)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/client.py", line 871, in get_bucket
    bucket.reload(
  File "/usr/lib/python3.12/contextlib.py", line 81, in inner
    return func(*args, **kwds)
           ^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/bucket.py", line 1088, in reload
    super(Bucket, self).reload(
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/_helpers.py", line 300, in reload
    api_response = client._get_resource(
                   ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/google/cloud/storage/client.py", line 464, in _get_resource
    return self._connection.api_request(/staging/',
        temp_location='gs://banded-edge-437103-i9/temp/',
        region='us-central1',
        streaming =True,
        runner='DataflowRunner'
    )

    p = beam.Pipeline(options=options)

    # Read from Pub/Sub without windowing
    lines = (
        p
        | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/real-time-subscription')  # Replace with your subscription ID
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
