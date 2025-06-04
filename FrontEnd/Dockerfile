# Use official Node image
FROM node:18

# Set working directory
WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy rest of the app
COPY . .

# Expose Vite dev server port
EXPOSE 3000

