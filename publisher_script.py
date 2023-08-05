import time
import random
import os
from google.cloud import pubsub_v1

project_id = 'steady-tracer-392814'
topic_id = 'temperature-sensor'

# Obtain an access token
access_token = os.popen('gcloud auth print-access-token --impersonate-service-account=pubsub-service-account@steady-tracer-392814.iam.gserviceaccount.com').read().strip()

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

while True:
    temperature = random.uniform(20, 45)  # Generate a random temperature between 20 and 45 degrees Celsius
    data = f'Temperature: {temperature:.2f}°C'
    publisher.publish(topic_path, data.encode('utf-8'))
    print(f'Published: {data}')
    time.sleep(1800)  # Sleep for 30 minutes
