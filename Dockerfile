FROM python:3.9-slim

# Add a non-root user
RUN useradd -m nonroot
USER nonroot

WORKDIR /app

COPY app.py .

COPY . .

RUN pip install flask concurrent-log-handler

EXPOSE 5000

CMD ["python", "app.py"]
