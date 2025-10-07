import time
import logging
from datetime import datetime
from extract import extract_data
from load import load_data

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/app/logs/etl_pipeline.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    logger.info("Starting ELT Pipeline")
    logger.info("Pipeline started at: " + str(datetime.now()))
    
    # Wait for database to be ready
    logger.info("Waiting for database to be ready...")
    time.sleep(10)
    
    try:
        # Step 1: Extract the data
        logger.info("STEP 1: EXTRACT")
        data = extract_data()
        logger.info("Extracted " + str(len(data)) + " rows successfully")
        
        # Step 2: Load the data (DBT will transform it later)
        logger.info("STEP 2: LOAD")
        load_data(data)
        logger.info("Loaded " + str(len(data)) + " rows to staging table")
        
        # Success message
        logger.info("EL Pipeline Completed Successfully!")
        logger.info("DBT will now handle transformations...")
        
    except Exception as e:
        logger.error("Pipeline failed with error: " + str(e))
        raise

# This runs the main function when you execute the script
main()
