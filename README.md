# ELT Pipeline with Docker, PostgreSQL & DBT

A fully containerized ELT (Extract, Load, Transform) pipeline that processes sales data using Python, PostgreSQL, and DBT.

## Author
Temitope Fafure
Data Engineering Student at CDE

## What This Does

- Extracts sales data from CSV files
- Loads it into PostgreSQL database
- Transforms it using DBT (Data Build Tool)
- Runs automatically every day at 12:00 AM
- Provides comprehensive logging for debugging

## Technologies Used

- **Python 3.9** - Data extraction and loading
- **PostgreSQL 15** - Database storage
- **DBT 1.5.0** - Data transformation
- **Docker & Docker Compose** - Containerization

## Architecture

The pipeline consists of 3 main containers:

1. **PostgreSQL Container** - Database for storing raw and transformed data
2. **Python ETL Container** - Extracts from CSV and loads to PostgreSQL
3. **DBT Container** - Transforms raw data into analytics-ready tables

## Quick Start

### Prerequisites

- Docker Desktop installed and running
- Git installed

### Installation

1. Clone this repository:
```bash
git clone https://github.com/temmywork/elt-pipeline-project.git
cd elt-pipeline-project
