import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.logger import logger  # Import the custom logger

def analyze_sales_trend(input_file='data/sales_data.csv', output_dir='images'):
    """
    Analyzes sales trends over time and saves the results.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Directory to save the outputs.

    Returns:
        None
    """
    try:
        logger.info("Starting sales trend analysis.")

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory ensured: {output_dir}")

        # Load the sales data
        df = pd.read_csv(input_file)
        logger.info(f"Sales data loaded from {input_file}")

        # Add a 'month' column
        df['month'] = pd.to_datetime(df['order_date']).dt.to_period('M')
        logger.info("Added 'month' column to the dataset.")

        # Aggregate sales by month
        sales_trend = df.groupby('month')['sales_amount'].sum().reset_index()
        sales_trend['month'] = sales_trend['month'].dt.to_timestamp()
        logger.info("Aggregated sales by month.")

        # Create a visualization
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=sales_trend, x='month', y='sales_amount', marker='o')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Month')
        plt.ylabel('Total Sales Amount')
        plt.grid()
        logger.info("Visualization for sales trend created.")

        # Save the visualization
        sales_trend_visualization_file = f"{output_dir}/sales_trend.png"
        plt.savefig(sales_trend_visualization_file)
        logger.info(f"Sales trend visualization saved to {sales_trend_visualization_file}")
        plt.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    analyze_sales_trend()