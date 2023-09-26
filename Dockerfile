# Use the official Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /COURSE_API

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the entire Django project directory into the container
COPY . .

# Run the Django development server
CMD ["python3", "manage.py", "runserver", "127.0.0.1:8000"]
