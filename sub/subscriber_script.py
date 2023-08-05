from google.cloud import pubsub_v1, bigquery

# Create a SubscriberClient
subscriber = pubsub_v1.SubscriberClient()

project_id = 'steady-tracer-392814'
subscription_id = 'temperature-sensor-sub'

# The subscription path
subscription_path = f"projects/{project_id}/subscriptions/{subscription_id}"

# Initialize BigQuery client
bigquery_client = bigquery.Client()

# Define dataset and table names
dataset_id = 'iot_dataset'
table_id = 'temperature_table'

# Get the table reference
table_ref = bigquery_client.dataset(dataset_id).table(table_id)

def callback(message):
    data = message.data.decode("utf-8")
    temperature = float(data.split()[1][:-2])  # Extract temperature from the message

    rows_to_insert = [
    {"temperature":temperature} ]

    errors = bigquery_client.insert_rows_json(
        table_ref, rows_to_insert, row_ids=[None] * len(rows_to_insert)
    )  # Make an API request.
    if errors == []:
        print("New rows have been added.")
    else:
        print("Encountered errors while inserting rows: {}".format(errors))

    # Acknowledge the message
    message.ack()


# Subscribe to the subscription
future = subscriber.subscribe(subscription_path, callback=callback)

# Keep the script running to receive messages
try:
    future.result()
except KeyboardInterrupt:
    future.cancel()
