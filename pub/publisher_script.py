import time
import random
from google.cloud import pubsub_v1
import os
from datetime import datetime

project_id = os.environ.get('project_id')
topic_id = os.environ.get('topic_id')

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_id)

print("Publishing a temperature: ")

while True:
    date = datetime.now()
    temperature = random.uniform(20, 45)  # Generate a random temperature between 20 and 45 degrees Celsius
    data = f'Temperature: {temperature:.2f}°C {date}'
    publisher.publish(topic_path, data.encode('utf-8'))
    print(f'Published: {data}')
    time.sleep(1800)  # Sleep for 30 minutes
