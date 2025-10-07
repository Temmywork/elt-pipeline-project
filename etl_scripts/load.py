import pandas as pd
from sqlalchemy import create_engine
import logging
import os

logger = logging.getLogger(__name__)

def load_data(df):
    """
    Load raw data into PostgreSQL staging table
    No transformations - just raw data
    DBT will handle transformations later
    """
    logger.info("Starting data load to PostgreSQL...")
    
    try:
        # Get database credentials from environment variables
        db_host = os.getenv('DB_HOST', 'postgres_db')
        db_port = os.getenv('DB_PORT', '5432')
        db_name = os.getenv('DB_NAME', 'elt_database')
        db_user = os.getenv('DB_USER', 'postgres')
        db_password = os.getenv('DB_PASSWORD', 'postgres')
        
        # Create connection string
        connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        logger.info(f"Connecting to database at {db_host}:{db_port}/{db_name}")
        
        # Create engine
        engine = create_engine(connection_string)
        
        # Load to staging table (raw data, no transformations)
        table_name = 'raw_sales'
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
        logger.info(f"Successfully loaded {len(df)} rows to table '{table_name}'")
        logger.info(f"Table schema: {list(df.columns)}")
        
        # Verify the load
        from sqlalchemy import text
        with engine.connect() as conn:
            result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
            count = result.fetchone()[0]
            logger.info(f"Verification: {count} rows in database")
        
        engine.dispose()
        logger.info("Database connection closed")
        
    except Exception as e:
        logger.error(f"Error during data load: {str(e)}")
        raise
