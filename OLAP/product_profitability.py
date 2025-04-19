import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.logger import logger  # Import the custom logger

def rank_product_profitability(input_file='data/sales_data.csv', output_dir='images'):
    """
    Ranks products by profitability and saves the results.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Directory to save the outputs.

    Returns:
        None
    """
    try:
        logger.info("Starting product profitability ranking.")

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory ensured: {output_dir}")

        # Load the sales data
        df = pd.read_csv(input_file)
        logger.info(f"Sales data loaded from {input_file}")

        # Rank products by total profit
        product_profit = df.groupby('product_category')['profit'].sum().reset_index()
        product_profit = product_profit.sort_values(by='profit', ascending=False)
        logger.info("Ranked products by total profit.")

        # Create a visualization
        plt.figure(figsize=(8, 5))
        sns.barplot(data=product_profit, x='profit', y='product_category')
        plt.title('Most Profitable Product Categories')
        plt.xlabel('Total Profit')
        plt.ylabel('Product Category')
        plt.tight_layout()
        logger.info("Visualization for product profitability created.")

        # Save the visualization
        product_profit_visualization_file = f"{output_dir}/product_profit.png"
        plt.savefig(product_profit_visualization_file)
        logger.info(f"Product profitability visualization saved to {product_profit_visualization_file}")
        plt.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    rank_product_profitability()