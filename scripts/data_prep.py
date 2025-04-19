import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from utils.logger import logger  # Import the custom logger


def generate_sales_data(output_file='data/sales_data.csv', num_records=200):
    """
    Generates a sample sales dataset and saves it to a CSV file.

    Parameters:
        output_file (str): The name of the output CSV file.
        num_records (int): The number of records to generate.

    Returns:
        None
    """
    try:
        logger.info("Starting sales data generation.")
        
        # Set a seed for reproducibility
        np.random.seed(42)

        # Define product categories, regions, and payment methods
        product_categories = ['Electronics', 'Clothing', 'Home Goods', 'Books']
        regions = ['North', 'South', 'East', 'West']
        payment_methods = ['Credit Card', 'PayPal', 'Bank Transfer', 'Cash']

        # Define the date range for the last year
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        dates = pd.date_range(start=start_date, end=end_date, freq='D')

        # Create random data
        data = {
            'order_id': [f'ORD{i:05d}' for i in range(num_records)],
            'order_date': np.random.choice(dates, size=num_records),
            'product_category': np.random.choice(product_categories, size=num_records),
            'region': np.random.choice(regions, size=num_records),
            'sales_amount': np.random.uniform(10, 500, size=num_records),
            'cost': np.random.uniform(5, 200, size=num_records),
            'payment_method': np.random.choice(payment_methods, size=num_records),
        }

        # Create a DataFrame
        df = pd.DataFrame(data)

        # Ensure order_date contains only the date
        df['order_date'] = df['order_date'].dt.date

        # Round sales_amount and cost to 2 decimal places
        df['sales_amount'] = df['sales_amount'].round(2)
        df['cost'] = df['cost'].round(2)

        # Calculate profit
        df['profit'] = (df['sales_amount'] - df['cost']).round(2)

        # Save to CSV
        df.to_csv(output_file, index=False)

        logger.info(f"Sample data saved to {output_file}.")

    except Exception as e:
        logger.error(f"An error occurred while generating the sales data: {e}")
        print(f"An error occurred while generating the sales data: {e}")

# Run the function
if __name__ == "__main__":
    generate_sales_data()