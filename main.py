# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Ensure 'diabetes.csv' is in your working directory or update the path accordingly.
data = pd.read_csv('diabetes.csv')


# Function 1: Histogram of BMI distribution
def plot_bmi_distribution(data):
    """
    Plots the distribution of BMI using a histogram.

    Parameters:
        data (DataFrame): The DataFrame containing the dataset with BMI column.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data['BMI'], bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of BMI')
    plt.xlabel('BMI')
    plt.ylabel('Frequency')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


# Function 2: Scatter plot of Glucose vs. Age with color-coded Outcome
def plot_glucose_vs_age(data):
    """
    Creates a scatter plot of Glucose levels vs. Age, color-coded by diabetes Outcome.

    Parameters:
        data (DataFrame): The DataFrame containing the dataset with Glucose, Age, and Outcome columns.
    """
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Age', y='Glucose', hue='Outcome', data=data, palette='coolwarm')
    plt.title('Glucose Levels vs. Age (Color-coded by Diabetes Outcome)')
    plt.xlabel('Age')
    plt.ylabel('Glucose Level')
    plt.legend(title='Diabetes Outcome', loc='upper left')
    plt.grid(True)
    plt.show()


# Function 3: Heatmap of correlation matrix
def plot_correlation_heatmap(data):
    """
    Displays a heatmap of the correlation matrix for the dataset's features.

    Parameters:
        data (DataFrame): The DataFrame containing the dataset.
    """
    plt.figure(figsize=(10, 8))
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='viridis', vmin=-1, vmax=1)
    plt.title('Correlation Matrix Heatmap')
    plt.show()


# Generating the plots
plot_bmi_distribution(data)
plot_glucose_vs_age(data)
plot_correlation_heatmap(data)
