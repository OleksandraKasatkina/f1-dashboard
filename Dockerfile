FROM python:3.13-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# working directory
WORKDIR /app

# requirements file and dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# application code goes into the container
COPY . .

EXPOSE 8000

# command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]