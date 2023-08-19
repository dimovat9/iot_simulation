from google.cloud import pubsub_v1
import os
from send_to_slack import sendMessage

# Create a SubscriberClient
subscriber = pubsub_v1.SubscriberClient()

project_id = os.environ.get('project_id')
subscription_id = os.environ.get('sub_alert_id')

# The subscription path for the alert
subscription_path = f"projects/{project_id}/subscriptions/{subscription_id}"


def callback(message):
    data = message.data.decode("utf-8")
    temperature = float(data.split()[1][:-2]) 
    date= data.split()[2] +' ' + data.split()[3]

    if (temperature > 35.00):
        sendMessage("Temeprature Alert","Current temperature: " + str(temperature) + " at " + date)

    # Acknowledge the message
    message.ack()


# Subscribe to the subscription
future = subscriber.subscribe(subscription_path, callback=callback)

# Keep the script running to receive messages
try:
    future.result()
except KeyboardInterrupt:
    future.cancel()
