const mqtt = require('mqtt');
const Temperature = require('./db');
const express = require('express');
const app = express();

const TOPIC = 'iot/temperature';
const client = mqtt.connect('mqtt://broker.hivemq.com'); // Use any public MQTT broker

client.on('connect', () => {
  console.log('Connected to MQTT broker');
  client.subscribe(TOPIC);
});

client.on('message', (topic, message) => {
    if (topic === TOPIC) {
      console.log('Received MQTT message:', message.toString()); // Debugging line
      const temperature = parseFloat(message.toString());
      const newTemperature = new Temperature({ temperature });
      newTemperature.save()
        .then(() => console.log(`Saved: ${temperature}°C`))
        .catch(error => console.error('Error saving data:', error));
    }
  });

// Define your route handler for the root URL
app.get('/iot', (req, res) => {
    res.send('Welcome to the IoT Simulation'); // You can customize the response here
  });
  
  const port = 3000; // Make sure the port is set to 3000
  app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });
  