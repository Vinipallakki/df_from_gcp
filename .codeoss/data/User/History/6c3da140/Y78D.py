import random
import time  # Import the time module
from google.cloud import pubsub_v1

project_id = 'banded-edge-437103-i9'
topic_id = 'topic_1'  # Replace with your topic ID

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Function to generate sample data
def generate_sample_data(num_records):
    names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Isaac', 'Jack']
    sample_data = []
    for _ in range(num_records):
        name = random.choice(names)
        age = random.randint(20, 60)  # Random age between 20 and 60
        salary = random.randint(40000, 120000)  # Random salary between 40k and 120k
        sample_data.append(f'{name},{age},{salary}')
    return sample_data

# Generate 100 records
data = generate_sample_data(100)

# Publish records to Pub/Sub with a 1-second delay
for record in data:
    # Data must be a bytestring
    publisher.publish(topic_path, record.encode('utf-8'))
    print(f'Published {record} to {topic_path}')
    time.sleep(1)  # Delay of 1 second
