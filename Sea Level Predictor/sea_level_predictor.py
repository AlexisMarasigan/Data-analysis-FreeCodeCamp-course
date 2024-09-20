import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data Points')

    # Create first line of best fit (from the full dataset)
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_full = pd.Series(range(1880, 2051))
    y_pred_full = intercept + slope * x_pred_full
    plt.plot(x_pred_full, y_pred_full, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit (from year 2000 onward)
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = pd.Series(range(2000, 2051))
    y_pred_2000 = intercept_2000 + slope_2000 * x_pred_2000
    plt.plot(x_pred_2000, y_pred_2000, 'green', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Customize the ticks
    plt.xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # Save plot and return for testing
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()
