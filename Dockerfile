# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Define environment variable
ENV PYTHON Web

# Copy the current directory contents into the container at /app
ADD . /code/
