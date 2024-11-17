# Step 1: Use an official Python runtime as a parent image
FROM python:3.10-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the current project files to the container
COPY . /app/.

# Step 4: Install Python dependencies
RUN python -m venv /opt/venv \
    && . /opt/venv/bin/activate \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Step 5: Expose the port your app runs on (usually 8000 for Django)
EXPOSE 8000

# Step 6: Set the default command to run your Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
