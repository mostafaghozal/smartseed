# Use the official Node.js image as a base
FROM node:12

# Set the working directory inside the container
WORKDIR /app

# Copy the package.json and package-lock.json (if available) into the working directory
COPY package*.json ./

# Install dependencies with bypassing engine checks
RUN npm install --legacy-peer-deps --engine-strict=false

# Copy the rest of the application code
COPY . .

# Install node-sass if it's not properly installed
RUN npm install node-sass --save-dev

# Expose the port the app runs on
EXPOSE 4200

# Build the Angular application
RUN npm run build

# Command to run the Angular application
CMD ["npm", "start"]
