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
