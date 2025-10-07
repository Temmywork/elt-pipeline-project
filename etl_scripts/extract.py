import pandas as pd
import logging

logger = logging.getLogger(__name__)

def extract_data():
    """
    Extract data from CSV file
    """
    logger.info("Starting data extraction...")
    
    try:
        # Read CSV file
        df = pd.read_csv('/data/sales_data.csv')
        
        logger.info(f"Successfully extracted {len(df)} rows from sales_data.csv")
        logger.info(f"Columns: {list(df.columns)}")
        logger.info(f"Data types:\n{df.dtypes}")
        
        # Basic data quality checks
        null_counts = df.isnull().sum()
        if null_counts.any():
            logger.warning(f"Found null values:\n{null_counts[null_counts > 0]}")
        
        return df
        
    except FileNotFoundError:
        logger.error("CSV file not found at /data/sales_data.csv")
        raise
    except Exception as e:
        logger.error(f"Error during extraction: {str(e)}")
        raise
