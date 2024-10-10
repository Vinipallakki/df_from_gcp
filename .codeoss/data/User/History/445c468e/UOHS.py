# import apache_beam as beam
# from apache_beam.options.pipeline_options import PipelineOptions
# from apache_beam.io.gcp.bigquery import WriteToBigQuery
# from apache_beam.transforms.window import FixedWindows
# import csv

# def parse_csv(line):
#     """Parse CSV line into a dictionary."""
#     row = list(csv.reader([line]))[0]
#     return {
#         'name': row[0],
#         'age': int(row[1]),  # Convert age to integer
#         'salary': float(row[2])  # Convert salary to float
#     }

# def run():
#     options = PipelineOptions(
#         project='banded-edge-437103-i9',  # Replace with your GCP project ID
#         job_name='dataflow-etl-job',
#         staging_location='gs://banded-edge-437103-i9/staging/',
#         temp_location='gs://banded-edge-437103-i9/temp/',
#         region='us-central1',
#         runner='DataflowRunner'
#     )

#     p = beam.Pipeline(options=options)

#     # Read from Pub/Sub and apply windowing
#     lines = (
#         p
#         | 'Read from PubSub' >> beam.io.ReadFromPubSub(subscription='projects/banded-edge-437103-i9/subscriptions/your-subscription-id')  # Replace with your subscription ID
#         | 'Parse CSV' >> beam.Map(parse_csv)
#         | 'Window into fixed intervals' >> beam.WindowInto(
#             FixedWindows(5)  # Use a fixed window of 5 seconds
#         )
#         | 'Format for BigQuery' >> beam.Map(lambda x: {
#             'name': x['name'],
#             'age': x['age'],
#             'salary': x['salary']
#         })
#     )

#     # Write transformed data to BigQuery
#     lines | 'Write to BigQuery' >> WriteToBigQuery(
#         table='banded-edge-437103-i9:first.second',  # Replace with your BigQuery project:dataset.table
#         schema='name:STRING, age:INTEGER, salary:FLOAT',
#         create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
#         write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
#     )

#     p.run().wait_until_finish()

# if __name__ == '__main__':
#     run()


import com.google.api.services.bigquery.model.TableRow;
import org.apache.beam.sdk.Pipeline;
import org.apache.beam.sdk.io.gcp.bigquery.BigQueryIO;
import org.apache.beam.sdk.io.gcp.pubsub.PubsubIO;
import org.apache.beam.sdk.options.PipelineOptions;
import org.apache.beam.sdk.options.PipelineOptionsFactory;
import org.apache.beam.sdk.options.StreamingOptions;
import org.apache.beam.sdk.transforms.DoFn;
import org.apache.beam.sdk.transforms.MapElements;
import org.apache.beam.sdk.transforms.ParDo;
import org.apache.beam.sdk.transforms.windowing.FixedWindows;
import org.apache.beam.sdk.transforms.windowing.Window;
import org.apache.beam.sdk.values.TypeDescriptor;
import org.joda.time.Duration;

import java.util.Arrays;

public class DataflowPipeline {

    public static class ParseCsvFn extends DoFn<String, TableRow> {
        @ProcessElement
        public void processElement(@Element String line, OutputReceiver<TableRow> out) {
            // Split CSV line by commas
            String[] columns = line.split(",");
            if (columns.length == 3) {
                TableRow row = new TableRow()
                        .set("name", columns[0])
                        .set("age", Integer.parseInt(columns[1]))
                        .set("salary", Float.parseFloat(columns[2]));
                out.output(row);
            }
        }
    }

    public static void main(String[] args) {

        // Create pipeline options
        PipelineOptions options = PipelineOptionsFactory.fromArgs(args).withValidation().as(StreamingOptions.class);
        options.setProject("banded-edge-437103-i9"); // Replace with your GCP project ID
        options.setJobName("dataflow-etl-job");
        ((StreamingOptions) options).setStreaming(true);
        options.setTempLocation("gs://banded-edge-437103-i9/temp/");

        // Create the pipeline
        Pipeline p = Pipeline.create(options);

        // Read from Pub/Sub
        p.apply("ReadFromPubSub", PubsubIO.readStrings()
                .fromSubscription("projects/banded-edge-437103-i9/subscriptions/your-subscription-id")) // Replace with your Pub/Sub subscription ID
         // Parse CSV and apply windowing
         .apply("Window", Window.into(FixedWindows.of(Duration.standardSeconds(5))))
         .apply("ParseCSV", ParDo.of(new ParseCsvFn()))
         // Write to BigQuery
         .apply("WriteToBigQuery", BigQueryIO.writeTableRows()
                .to("banded-edge-437103-i9:first.second") // Replace with your BigQuery project:dataset.table
                .withSchema(BigQueryIO.parseSchema("name:STRING, age:INTEGER, salary:FLOAT"))
                .withCreateDisposition(BigQueryIO.Write.CreateDisposition.CREATE_IF_NEEDED)
                .withWriteDisposition(BigQueryIO.Write.WriteDisposition.WRITE_APPEND)
        );

        // Run the pipeline
        p.run().waitUntilFinish();
    }
}
