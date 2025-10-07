FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY etl_scripts/ /app/

RUN mkdir -p /data /app/logs

RUN chmod 777 /app/logs

CMD ["python", "main_etl.py"]
