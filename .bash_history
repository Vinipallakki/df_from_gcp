gcloud run deploy trigger-cf-sheet-to-bq --region=YOUR_REGION --source .
gcloud auth list
gcloud config set account
gcloud config list project
gcloud auth list
gcloud config list project
gcloud config set project banded-edge-437103-i9
gcloud run deploy trigger-cf-sheet-to-bq --region=YOUR_REGION --source .
gcloud run deploy trigger-cf-sheet-to-bq --region=asia-south1 --source .
gcloud functions add-invoker-policy-binding function-1       --region="us-central1"       --member="627003217872-compute@developer.gserviceaccount.com"
gcloud functions add-invoker-policy-binding function-1     --region="us-central1"     --member="serviceAccount:627003217872-compute@developer.gserviceaccount.com"
vi export_bq_to_gcs.py
cat export_bq_to_gcs.py
clear
ls
gcloud functions deploy export_bq_to_gcs     --runtime python310     --trigger-topic first \ 
gcloud functions deploy export_bq_to_gcs     --runtime python310     --trigger-topic first     --set-env-vars PROJECT_ID=banded-edge-437103-i9,DATASET_ID=gcp_dataeng_demos,TABLE_ID=demo_cf,BUCKET_NAME=banded-edge-437103-i9     --timeout=540s
clear
ls
vi export_bq_to_gcs.py
vi main.py
vi requirements.txt
gcloud functions deploy export_bq_to_gcs     --runtime python310     --trigger-topic first     --set-env-vars PROJECT_ID=banded-edge-437103-i9,DATASET_ID=gcp_dataeng_demos,TABLE_ID=demo_cf,BUCKET_NAME=banded-edge-437103-i9     --timeout=540s
clear
gcloud functions deploy main     --runtime python310     --trigger-topic first     --set-env-vars PROJECT_ID=banded-edge-437103-i9,DATASET_ID=gcp_dataeng_demos,TABLE_ID=demo_cf,BUCKET_NAME=banded-edge-437103-i9     --timeout=540s
gcloud run deploy function-4     --image gcr.io/YOUR_PROJECT_ID/my-function-image     --platform managed     --region YOUR_REGION     --set-env-vars KEY=VALUE     --memory 512Mi     --timeout 540s
clear
vi dataflow_etl.py
ls
python dataflow_etl.py
clear
python3 -m venv beam_env
source beam_env/bin/activate
pip install apache-beam[gcp]
ls
clear
ls
python dataflow_etl.py
clear
cleear
ls
python pub.py
pip install pubsub
python pub.py
pip show google-cloud-pubsub
pip install google-cloud-pubsub
pip3 install google-cloud-pubsub
python pub.py
clear
ls
python real_dataflow_etl.py
ls
pip install apache-beam[gcp]
python real_dataflow_etl.py
clear
ls
python real_dataflow_etl.py
c;ear
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
cat real_dataflow_etl.py
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
ls
python pub.py
gcloud pubsub topics create real-time-topic
gcloud pubsub subscriptions create real-time-subscription --topic=real-time-topic
bq mk my_realtime_dataset
clar
clear
bq mk --table my_realtime_dataset.realtime_table name:STRING, age:INTEGER, salary:FLOAT
bq mk --table my_realtime_dataset.realtime_table --schema 'name:STRING, age:INTEGER, salary:FLOAT'
bq mk --table my_realtime_dataset.realtime_table name:STRING,age:INTEGER,salary:FLOAT
ls
python pubs.py
ls
python real_dataflow_etl.py
ls
python pubs.py
clear
python real_dataflow_etl.py
clear
ls
javac real_dataflow_etl.py.java
javac real_dataflow_etl.java
clear
ls
javac DataflowPipeline.java
ls
rm DataflowPipeline.java
ls
clear
python real_dataflow_etl.py
ls
python pubs.py
clear
python real_dataflow_etl.py
clear
ls
pwd
gcloud auth activate-service-account SERVICE_ACCOUNT@DOMAIN.COM --key-file=/home/youwantsomethings/banded-edge-437103-i9-2b57fbf82072.json --project=banded-edge-437103-i9
clear
gcloud auth activate-service-account 627003217872-compute@developer.gserviceaccount.com --key-file=/home/youwantsomethings/banded-edge-437103-i9-2b57fbf82072.json --project=banded-edge-437103-i9
clear
python real_dataflow_etl.py
cleaer
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
gsutil ls
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
gcloud auth activate-service-account hello-123@banded-edge-437103-i9.iam.gserviceaccount.com
gcloud iam service-accounts enable hello-123@banded-edge-437103-i9.iam.gserviceaccount.com
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
python real_dataflow_etl.py
clear
gcloud auth login
gcloud auth application-default login
clear
python real_dataflow_etl.py
ls
clear
gcloud dataflow jobs run testjob --gcs-location gs://hello_hi_9665/templete --max-workers 10  
ls
python pubs.py
python real_dataflow_etl.py
clea
clear
python real_dataflow_etl.py
python pubs.py
clear
ls
python real_dataflow_etl.py
clear
gcloud dataflow jobs run testjobs --gcs-location gs://hello_hi_9665/templete --max-workers 10
ls
python pubs.py
clear
python pubs.py
clear
gcloud dataflow jobs run testjobs --gcs-location gs://hello_hi_9665/templete --max-workers 10
python real_dataflow_etl.py
gcloud dataflow jobs run testjobss --gcs-location gs://hello_hi_9665/templete --max-workers 10
source /home/youwantsomethings/beam_env/bin/activate
git config --global user.name "Vinipallakki"
git config --global user.email "vinayakapallakki@gmail.com" 
git remote add origin https://github.com/Vinipallakki/df_from_gcp.git
git remote -v
origin  https://github.com/Vinipallakki/df_from_gcp.git (fetch)
origin  https://github.com/Vinipallakki/df_from_gcp.git (push)
origin  https://github.com/Vinipallakki/df_from_gcp.git
https://github.com/Vinipallakki/df_from_gcp.git
clear
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/Vinipallakki/df_from_gcp.git
git push -u origin master
git push -u origin main
git pull
git pull origin main
git config pull.rebase false
git pull origin main
git pull origin main --allow-unrelated-histories
git commit -m "Resolved merge conflicts"
gcloud pubsub topics publish temperature_topic --message "{\"timestamp\": \"2024-10-10T10:32:02Z\", \"temperature\": 25.6}"
ls
python iot_real_time.py
pip install apache-beam[gcp]
python iot_real_time.py
import apache_beam as beam
print(beam.__version__)
python --version
pip install virtualenv
virtualenv myvenv
source myvenv/bin/activate
pip install apache-beam[gcp]
python iot_real_time.py
pip install apache-beam[gcp]
ls
pwd
python /home/youwantsomethings/iot_real_time.py
pip install apache-beam
pip install apache-beam[gcp]
clear
python /home/youwantsomethings/iot_real_time.py
pip install --upgrade apache-beam[gcp]
clear
vi test.py
python test.py
ls
python iot_real_time.py
clar
clear
python iot_real_time.py
gcloud iam service-accounts enable 627003217872-compute@developer.gserviceaccount.com
python iot_real_time.py
clear
python iot_real_time.py
pip show apache-beam
python iot_real_time.py
ls
clear
ls
vi stream.py
rm stream.py
ls
vi stream.py
ls
vi req.sh
vi pub.sh
clear
ls
bash pub.sh
vi user_generator.py
bash pub.sh
pip install faker
bash pub.sh
clear
ls
python3 -m pip install -q --upgrade pip setuptools wheel
python3 -m pip install apache-beam[gcp]
# Create GCS buckets and BQ dataset
cd $BASE_DIR/../..
source create_streaming_sinks.sh
ls
cd home
ls
cd youwantsomethings
;s
ls
cd dataflow_python
ls
cd dataflow_python
ls
cd 5_Streaming_Analytics/
ls
cd solution/
ls
python3 streaming_minute_traffic_SQL_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
export PROJECT_ID=$(gcloud config get-value project)
export REGION=Region
export BUCKET=gs://${PROJECT_ID}
export PIPELINE_FOLDER=${BUCKET}
export RUNNER=DataflowRunner
export PUBSUB_TOPIC=projects/${PROJECT_ID}/topics/my_topic
export TABLE_NAME=${PROJECT_ID}:logs.minute_traffic
bash generate_streaming_events.sh 
clear
cleaer
clear
ls
python streaming_minute_traffic_pipeline.py
pwd
cd ..
l
cd lab
ls
python3 streaming_minute_traffic_SQL_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
ls
python3 streaming_minute_traffic_SQL_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
ls
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
clear
ls
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
clear
ls
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
clear
ls
cd dataflow_python
ls
cd 5_Streaming_Analytics
ls
cd solution
ls
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
export PROJECT_ID=$(gcloud config get-value project)
export REGION=Region
export BUCKET=gs://${PROJECT_ID}
export PIPELINE_FOLDER=${BUCKET}
export RUNNER=DataflowRunner
export PUBSUB_TOPIC=projects/${PROJECT_ID}/topics/my_topic
export TABLE_NAME=${PROJECT_ID}:logs.minute_traffic
clear
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
clear
ls
cd dataflow_python
ls
cd 5_Streaming_Analytics/
ls
cd solution/
ls
export PROJECT_ID=$(gcloud config get-value project)
export REGION=Region
export BUCKET=gs://${PROJECT_ID}
export PIPELINE_FOLDER=${BUCKET}
export RUNNER=DataflowRunner
export PUBSUB_TOPIC=projects/${PROJECT_ID}/topics/my_topic
export TABLE_NAME=${PROJECT_ID}:logs.minute_traffic
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
	--agg_table_name=minute_traffic
	--raw_table_name=minute_traffic
clear
export PROJECT_ID=$(gcloud config get-value project)
export REGION=Region
export BUCKET=gs://${PROJECT_ID}
export PIPELINE_FOLDER=${BUCKET}
export RUNNER=DataflowRunner
export PUBSUB_TOPIC=projects/${PROJECT_ID}/topics/my_topic
export TABLE_NAME=${PROJECT_ID}:logs.minute_traffic
export Agg=${PROJECT_ID}:logs.minute_traffic
export raw=${PROJECT_ID}:logs.minute_traffic
python3 streaming_minute_traffic_pipeline.py 	--project=${PROJECT_ID} 	--region=${REGION} 	--staging_location=${PIPELINE_FOLDER}/staging 	--temp_location=${PIPELINE_FOLDER}/temp 	--runner=${RUNNER} 	--input_topic=${PUBSUB_TOPIC} 	--table_name=${TABLE_NAME} 	--experiments=use_runner_v2
	--agg_table_name=${Agg}
	--raw_table_name=${raw
clear
python3 streaming_minute_traffic_pipeline.py     --project=${PROJECT_ID}     --region=${REGION}     --staging_location=${PIPELINE_FOLDER}/staging     --temp_location=${PIPELINE_FOLDER}/temp     --runner=${RUNNER}     --input_topic=${PUBSUB_TOPIC}     --agg_table_name=${Agg}     --raw_table_name=${raw}     --window_duration=60     --experiments=use_runner_v2
python3 streaming_minute_traffic_pipeline.py     --project=${PROJECT_ID}     --region=${REGION}     --staging_location=${PIPELINE_FOLDER}/staging     --temp_location=${PIPELINE_FOLDER}/temp     --runner=${RUNNER}     --input_topic=${PUBSUB_TOPIC}     --agg_table_name=${Agg}     --raw_table_name=${raw}     --window_duration=60  
--region=us-central1
clear
python3 streaming_minute_traffic_pipeline.py     --project=${PROJECT_ID}     --region=us-central1     --staging_location=${PIPELINE_FOLDER}/staging     --temp_location=${PIPELINE_FOLDER}/temp     --runner=${RUNNER}     --input_topic=${PUBSUB_TOPIC}     --agg_table_name=${Agg}     --raw_table_name=${raw}     --window_duration=60     --experiments=use_runner_v2
python3 streaming_minute_traffic_pipeline.py     --project=${PROJECT_ID}     --region=${REGION}     --staging_location=${PIPELINE_FOLDER}/staging     --temp_location=${PIPELINE_FOLDER}/temp     --runner=${RUNNER}     --input_topic=${PUBSUB_TOPIC}     --agg_table_name=${Agg}     --raw_table_name=${raw}     --window_duration=60  
clear
export PROJECT_ID=$(gcloud config get-value project)
export REGION=us-central1
export BUCKET=gs://${PROJECT_ID}
export PIPELINE_FOLDER=${BUCKET}
export RUNNER=DataflowRunner
export PUBSUB_TOPIC=projects/${PROJECT_ID}/topics/my_topic
export TABLE_NAME=${PROJECT_ID}:logs.minute_traffic
export Agg=${PROJECT_ID}:logs.minute_traffic
export raw=${PROJECT_ID}:logs.minute_traffic
ls
cd dataflow_python
ls
cd 5_
cd 5_Streaming_Analytics/
ls
cd ..
l
bash generate_streaming_events.sh
clear
ls
python streaming_event_generator.py
bash generate_streaming_events.sh
ls
bash generate_streaming_events.sh
python3 streaming_minute_traffic_pipeline.py     --project=${PROJECT_ID}     --region=${REGION}     --staging_location=${PIPELINE_FOLDER}/staging     --temp_location=${PIPELINE_FOLDER}/temp     --runner=${RUNNER}     --input_topic=${PUBSUB_TOPIC}     --agg_table_name=${Agg}     --raw_table_name=${raw}     --window_duration=60  
clear
LETE
vi input_data.csv
ls
gs cp input_data.csv gs://banded-edge-437103-i9
gsutil cp input_data.csv gs://banded-edge-437103-i9
gcloud dataproc clusters describe my-first-cluster \ 
gcloud dataproc clusters describe my-first-cluster --region=us-central1 --project=banded-edge-437103-i9
gcloud dataproc clusters describe my-first-cluster --region=us-central1 --project=banded-edge-437103-i9 --format="get(config.gceClusterConfig.serviceAccount)"
PROJECT_NUMBER-compute@developer.gserviceaccount.com
gcloud iam service-accounts list --filter="email:compute@developer.gserviceaccount.com"
ls
cat input_data.csv
clea
clear
gcloud config set project banded-edge-437103-i9
ls
clear
ls
pwd
gsutil cp /home/youwantsomethings/https_operators_demo_dag.py  gs://us-central1-dagggssss-c84ad20e-bucket/dags
ls
gsutil cp /home/youwantsomethings/from-http-gcs.py  gs://banded-edge-437103-i9
gsutil cp /home/youwantsomethings/from-http-gcs.py  gs://us-central1-dagggssss-c84ad20e-bucket/dags
ls
LS
ls
gsutil cp gs://us-central1-first-62967754-bucket/dags/airflow_monitoring.py
pwd
gsutil cp from-http-gcs.py gs://us-central1-first-62967754-bucket/dags/airflow_monitoring.py
gsutil cp from-http-gcs.py gs://us-central1-first-62967754-bucket/dags
pwd
gsutil cp gs://banded-edge-437103-i9/stock_data.json /home/youwantsomethings
ls
