# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set environment variables to prevent Python from buffering outputs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Step 3: Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Step 4: Set the working directory in the container
WORKDIR /app

# Step 5: Copy the current project files to the container
COPY . /app/.

# Step 6: Install Python dependencies
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Step 7: Expose the port your app runs on (usually 8000 for Django)
EXPOSE 8000

# Step 8: Set the default command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
