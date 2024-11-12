import time
import random
from google.cloud import pubsub_v1

# Set up your Google Cloud credentials and project information
project_id = "banded-edge-437103-i9"
topic_id = "employee-data-stream"

# Initialize the Publisher client
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

# Function to generate random employee data
def generate_employee_data():
    id_no = random.randint(1, 1000)
    name = f"Employee_{id_no}"
    age = random.randint(20, 60)
    salary = round(random.uniform(30000, 100000), 2)
    data = {
        "id_no": id_no,
        "name": name,
        "age": age,
        "salary": salary
    }
    return data

# Publish messages to Pub/Sub continuously
def publish_data():
    while True:
        # Generate employee data
        data = generate_employee_data()
        
        # Convert data to a string and encode to bytes
        message = str(data).encode("utf-8")
        
        # Publish the message
        future = publisher.publish(topic_path, message)
        
        # Log message ID for verification
        print(f"Published message ID: {future.result()}")
        
        # Sleep to simulate continuous data generation (adjust as needed)
        time.sleep()  # Publish every 5 seconds

if __name__ == "__main__":
    publish_data()

