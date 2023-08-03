# Use the official Node.js base image
FROM node:14

# Install pm2 globally
RUN npm install -g pm2

# Set working directory inside the container
WORKDIR /app

# Copy package.json and package-lock.json to the container and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the application source code to the container
COPY . .

# Expose the port your Node.js app is listening on (if needed)
EXPOSE 3000

# Start both applications using pm2
CMD ["pm2-runtime", "app.js", "--name", "nodejs-app", "--", "temperatureSensor.js"]
