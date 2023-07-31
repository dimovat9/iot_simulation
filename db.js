const mongoose = require('mongoose');



mongoose.set('strictQuery', false);

//Replace 'mongodb://localhost/iot_simulation' with your MongoDB connection string

mongoose.connect('mongodb://localhost/iot_simulation', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  serverSelectionTimeoutMS: 30000, // Set a higher timeout (e.g., 30 seconds)
});


const temperatureSchema = new mongoose.Schema({
  temperature: {
    type: Number,
    required: true
  },
  timestamp: {
    type: Date,
    default: Date.now
  }
});

const Temperature = mongoose.model('Temperature', temperatureSchema);

module.exports = Temperature;
