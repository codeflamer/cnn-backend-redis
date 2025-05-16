# What Neural Network Sees

A machine learning project that visualizes and interprets neural network predictions through an interactive web interface.

## Project Overview

This project consists of a backend service that caches neural network predictions from an API and a frontend interface that visualizes what the neural network sees. The system is deployed on Railway for reliable and scalable hosting.

## Backend

Link to backend - https://github.com/codeflamer/cnn-visualizer-backend

### Features

- Neural network prediction processing
- Redis caching for improved performance
- RESTful API endpoints

### Tech Stack

- Python
- FastAPI/Flask
- Redis

### Setup Instructions

1. Create and activate virtual environment:

   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   source venv/bin/activate      # On Unix/MacOS
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Configure environment variables:

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Set up Redis using Docker:

   ```bash
   # Pull the Redis Docker image
   docker pull redis:latest

   # Run Redis container
   docker run --name redis-cache -p 6379:6379 -d redis:latest

   # Verify Redis is running
   docker ps
   ```

   To stop Redis:

   ```bash
   docker stop redis-cache
   ```

   To remove Redis container:

   ```bash
   docker rm redis-cache
   ```

5. Run the development server:
   ```bash
   python main.py
   ```

## Frontend

Link to the frontend - https://github.com/codeflamer/cnn-visualizer

## Contact

Taiwo Tolulope - emryzs01@gmail.com

Project Link: [Convolutional Network Visualizer](https://cnn-visualizer.vercel.app/)
