FROM python:3.9-slim

# Add a non-root user
RUN useradd -m nonroot
USER nonroot

WORKDIR /app

# Copy and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py app.py

# Expose port and run the application
EXPOSE 5000
CMD ["python", "app.py"]
