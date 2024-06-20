# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install pip and pipenv
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pip install Cython

# Copy Pipfile and Pipfile.lock first to leverage Docker cache
COPY Pipfile Pipfile.lock /app/

# Install dependencies
RUN pipenv install --system --deploy

# Copy the rest of the application code
COPY . /app

# Make port 8081 available to the world outside this container
EXPOSE 8081

# Define environment variable
ENV NAME Chat_RPG_Game

# Run app.py when the container launches
CMD ["pipenv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8081"]
