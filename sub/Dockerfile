# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the container
COPY subscriber_script.py /app/

# Install the required dependencies
RUN pip install --no-cache-dir google-cloud-pubsub
RUN pip install --no-cache-dir google-cloud-bigquery

# Run the publisher script when the container starts
CMD ["python", "subscriber_script.py"]
