import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x='Year', y='CSIRO Adjusted Sea Level', data=df, label='Data')

    # Create first line of best fit using all data
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = pd.Series([year for year in range(1880, 2051)])
    line_all = slope_all * years_all + intercept_all
    plt.plot(years_all, line_all, 'r', label='Best Fit Line (1880-2050)')

    # Create second line of best fit using data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series([year for year in range(2000, 2051)])
    line_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, line_recent, 'g', label='Best Fit Line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()