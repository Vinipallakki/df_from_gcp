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
