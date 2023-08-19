# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the container
COPY alert_subscriber_script.py /app/
COPY send_to_slack.py /app/

# Install the required dependencies
RUN pip install --no-cache-dir google-cloud-pubsub
RUN pip install --no-cache-dir slackclient

# Run the publisher script when the container starts
CMD ["python", "alert_subscriber_script.py"]
