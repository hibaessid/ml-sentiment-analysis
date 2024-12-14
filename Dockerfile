# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all model files into the container
COPY . .

# Expose the ML model service port
EXPOSE 5001

# Command to run the ML model API
CMD ["python", "ml_model.py"]
