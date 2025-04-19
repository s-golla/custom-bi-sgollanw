import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils.logger import logger  # Import the custom logger

def analyze_regional_performance(input_file='data/sales_data.csv', output_dir='images'):
    """
    Analyzes regional performance in terms of sales and profit, and saves the results.

    Parameters:
        input_file (str): Path to the input CSV file.
        output_dir (str): Directory to save the outputs.

    Returns:
        None
    """
    try:
        logger.info("Starting regional performance analysis.")

        # Ensure the output directory exists
        os.makedirs(output_dir, exist_ok=True)
        logger.info(f"Output directory ensured: {output_dir}")

        # Load the sales data
        df = pd.read_csv(input_file)
        logger.info(f"Sales data loaded from {input_file}")

        # Aggregate sales and profit by region
        region_performance = df.groupby('region')[['sales_amount', 'profit']].sum().reset_index()
        logger.info("Aggregated sales and profit by region.")

        # Create visualizations
        fig, ax = plt.subplots(1, 2, figsize=(14, 6))

        # Total Sales by Region
        sns.barplot(
            data=region_performance,
            x='region',
            y='sales_amount',
            hue='region',  # Assign the x variable to hue
            ax=ax[0],
            palette=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'],  # Custom colors
            dodge=False  # Ensure bars are not split
        )
        ax[0].set_title('Total Sales by Region')
        ax[0].set_xlabel('Region')
        ax[0].set_ylabel('Total Sales Amount')
        if ax[0].legend_ is not None:  # Check if the legend exists
            ax[0].legend_.remove()  # Remove the legend
        logger.info("Total Sales by Region chart created.")

        # Total Profit by Region
        sns.barplot(
            data=region_performance,
            x='region',
            y='profit',
            hue='region',  # Assign the x variable to hue
            ax=ax[1],
            palette=['#9467bd', '#8c564b', '#e377c2', '#7f7f7f'],  # Custom colors
            dodge=False  # Ensure bars are not split
        )
        ax[1].set_title('Total Profit by Region')
        ax[1].set_xlabel('Region')
        ax[1].set_ylabel('Total Profit')
        if ax[1].legend_ is not None:  # Check if the legend exists
            ax[1].legend_.remove()  # Remove the legend
        logger.info("Total Profit by Region chart created.")

        # Save the visualization
        plt.tight_layout()
        region_performance_visualization_file = f"{output_dir}/region_performance.png"
        plt.savefig(region_performance_visualization_file)
        logger.info(f"Regional performance visualization saved to {region_performance_visualization_file}")
        plt.close()

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    analyze_regional_performance()