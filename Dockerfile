# Python image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to WD
COPY requirements.txt /app/

# Install dependencies in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port
EXPOSE 8080

# Run the app
CMD ["python", "app.py", "--host=0.0.0.0", "--port=${PORT:-8080}"]
