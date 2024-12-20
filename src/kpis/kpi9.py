
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


def kpi9(df):
    """# Each Crime Category over Years"""

    # Drop the first and last columns
    df = df.drop(df.columns[[0, -1]], axis=1)

    # Loop through the remaining columns for plotting
    for x in df.columns:
        if x == 'Year':
            continue  # Skip the 'Year' column
        plt.figure(figsize=(10, 6))  # Create a new figure for each plot
        sns.lineplot(x=df['Year'], y=df[x], data=df, marker='o')  # Add markers for better visibility
        plt.title(f'Trend of {x} Over Years')  # Set the title for each plot
        plt.xlabel('Year')  # Set x-axis label
        plt.ylabel(x)  # Set y-axis label
        plt.xticks(df['Year'], rotation=45)  # Rotate x-axis labels for better readability
        plt.grid()  # Add grid for better readability
        plt.tight_layout()  # Adjust layout to prevent overlap
        st.pyplot(fig)
