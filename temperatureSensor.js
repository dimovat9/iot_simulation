const mqtt = require('mqtt');
const client = mqtt.connect('mqtt://broker.hivemq.com'); // Use any public MQTT broker

const TEMPERATURE_TOPIC = 'iot/temperature';
const ALERT_TOPIC = 'iot/alert';

function getRandomTemperature(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function sendTemperatureData() {
  const temperature = getRandomTemperature(20, 50); // Generate random temperature data between 20°C and 50°C
  client.publish(TEMPERATURE_TOPIC, temperature.toString());
  console.log(`Published: ${temperature}°C`);

  if (temperature > 36) {
    const alertMessage = `Temperature Alert: High Temperature Detected! Current Temperature: ${temperature}°C`;
    client.publish(ALERT_TOPIC, alertMessage);
    console.log(`ALERT: ${alertMessage}`);
  }
}

// Call the sendTemperatureData function immediately to publish the first data
sendTemperatureData();

// Set interval to call the function every 30 minutes (30 minutes * 60 seconds * 1000 milliseconds)
const intervalTime = 30 * 60 * 1000;
setInterval(sendTemperatureData, 5000);
