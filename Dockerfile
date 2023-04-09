# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Create a non-root user named 'appuser' and set ownership of the /app directory
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser /app

# Switch to the 'appuser' user
USER appuser

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
