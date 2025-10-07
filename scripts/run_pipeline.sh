#!/bin/bash

echo "   Docker ELT Pipeline with DBT"


# Create logs directory if it doesn't exist
mkdir -p logs

# Clean up previous runs
echo "Cleaning up previous containers..."
docker-compose down -v

echo ""
echo "Building Docker images..."
docker-compose build

echo "Starting ELT Pipeline..."

# Run the entire pipeline
docker-compose up

echo "Checking results..."

# Check the transformed data
docker exec elt_postgres psql -U postgres -d elt_database -c "\dt"
echo ""
docker exec elt_postgres psql -U postgres -d elt_database -c "SELECT * FROM marts.sales_summary LIMIT 10;"

echo ""
echo "Pipeline completed!"
echo ""
echo "Check logs in the ./logs directory"
