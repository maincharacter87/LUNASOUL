FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=lunasoul.settings
ENV PYTHONUNBUFFERED=1



# Run the command to start the server
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000" ]