# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY aegis_backend/requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY aegis_backend /app/aegis_backend
COPY aegis_backend/core /app/core

# Collect static files
RUN python aegis_backend/manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Run the Django development server
CMD ["python", "aegis_backend/manage.py", "runserver", "0.0.0.0:8000"]
