FROM python:3.9-slim

# Install git (required by DBT)
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Install DBT with PostgreSQL adapter
RUN pip install --no-cache-dir \
    dbt-core==1.5.0 \
    dbt-postgres==1.5.0

WORKDIR /usr/app

COPY . /usr/app/

RUN mkdir -p /usr/app/logs

ENV DBT_PROFILES_DIR=/usr/app

CMD ["sh", "-c", "dbt run --profiles-dir /usr/app"]
