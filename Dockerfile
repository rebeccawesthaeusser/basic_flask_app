#Use an official Python runtime as a parent image
FROM python:3.6-windowsservercore

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory to /app
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Run app.py when the container launches
CMD ["python", "-u", "app.py"]


