FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY upload_to_drive.py .

ENTRYPOINT ["python", "/app/upload_to_drive.py"]
