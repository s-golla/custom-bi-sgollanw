import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.logger import logger  # Import the custom logger

def analyze_profit(input_file='data/sales_data.csv', output_dir='images'):
    """
    Analyzes profit by product category, region, and month, and saves the results.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Directory to save the outputs.

    Returns:
        None
    """
    try:
        logger.info("Starting profit analysis.")

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory ensured: {output_dir}")

        # Load the sales data
        df = pd.read_csv(input_file)
        logger.info(f"Sales data loaded from {input_file}")

        # Add a 'month' column
        df['month'] = pd.to_datetime(df['order_date']).dt.to_period('M')
        logger.info("Added 'month' column to the dataset.")

        # Aggregate profit by product category, region, and month
        profit_analysis = df.groupby(['product_category', 'region', 'month'])['profit'].sum().reset_index()
        logger.info("Aggregated profit by product category, region, and month.")

        # Create a visualization
        plt.figure(figsize=(12, 6))
        sns.barplot(data=profit_analysis, x='product_category', y='profit', hue='region')
        plt.title('Profit by Product Category and Region')
        plt.xlabel('Product Category')
        plt.ylabel('Total Profit')
        plt.legend(title='Region')
        plt.tight_layout()
        logger.info("Visualization for profit analysis created.")

        # Save the visualization
        profit_visualization_file = f"{output_dir}/profit_analysis.png"
        plt.savefig(profit_visualization_file)
        logger.info(f"Profit visualization saved to {profit_visualization_file}")
        plt.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    analyze_profit()