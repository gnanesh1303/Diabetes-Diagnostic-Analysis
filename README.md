# Diabetes Diagnostic Analysis

This repository contains the code and visualizations for an analysis of the **Pima Indians Diabetes Dataset**. This dataset was analyzed to understand key diagnostic trends related to diabetes, focusing on variables such as BMI, glucose levels, and age. 

## Project Overview

The goal of this project is to identify significant patterns and correlations within health-related diagnostic data. By visualizing the distribution and relationships of features associated with diabetes diagnosis, this analysis provides insights that can aid in diabetes prediction and prevention strategies.

## Dataset

The **Pima Indians Diabetes Dataset** was obtained from Kaggle. It includes various medical predictor variables and one target variable (`Outcome`), which indicates if a patient has diabetes (1) or not (0).

- **Link to Dataset**: [Pima Indians Diabetes Dataset on Kaggle](https://www.kaggle.com/uciml/pima-indians-diabetes-database)

## Project Structure

- `diabetes_analysis.py`: Contains Python code for loading, processing, and visualizing the dataset. 
- `README.md`: Project overview, installation instructions, and usage guide.

## Analysis and Visualization

The analysis includes the following visualizations:
1. **BMI Distribution Histogram**: Shows the distribution of BMI values in the dataset.
2. **Scatter Plot of Glucose vs. Age**: Examines the relationship between glucose levels and age, color-coded by diabetes diagnosis outcome.
3. **Correlation Matrix Heatmap**: Displays correlations among the dataset's features, highlighting significant associations with the outcome.

## Usage

To replicate this analysis, follow these steps:

### Prerequisites
- Python 3.x
- Packages: `pandas`, `matplotlib`, `seaborn`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/diabetes-diagnostic-analysis.git
    cd diabetes-diagnostic-analysis
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure that the `diabetes.csv` dataset is placed in the same directory as the Python file or update the path in the code.

### Running the Analysis

Run `diabetes_analysis.py` to generate all visualizations:

```bash
python diabetes_analysis.py
