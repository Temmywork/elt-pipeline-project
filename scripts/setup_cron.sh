#!/bin/bash

# Script to set up cron job for running ELT pipeline daily at 12:00 AM

echo "Setting up cron job for ELT pipeline..."

# Get the absolute path to the project directory
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

# Create a cron job entry
CRON_JOB="0 0 * * * cd $PROJECT_DIR && /usr/local/bin/docker-compose up >> $PROJECT_DIR/logs/cron.log 2>&1"

# Check if cron job already exists
(crontab -l 2>/dev/null | grep -F "docker-compose up") && echo "Cron job already exists" || {
    # Add the cron job
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    echo "Cron job added successfully!"
}

# Display current crontab
echo ""
echo "Current crontab:"
crontab -l

echo ""
echo "ELT Pipeline will run daily at 12:00 AM"
echo "Logs will be saved to: $PROJECT_DIR/logs/cron.log"
