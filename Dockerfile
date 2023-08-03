# Use the official Node.js base image
FROM node:14

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application source code to the container
COPY . .

# Expose the port your Node.js app is listening on
EXPOSE 3000

# Start the Node.js application
CMD ["node", "temperatureSensor.js"]
CMD ["node", "app.js"]
