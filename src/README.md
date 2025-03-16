# Src Folder

This folder contains the scripts and utility functions used across the project. These src codes are modular and designed to perform specific tasks such as data preprocessing, visualization, and statistical analysis.

---

## **Contents**
1. [Overview](#overview)
2. [File Descriptions](#file-descriptions)
3. [Usage](#usage)
4. [Dependencies](#dependencies)

---

## **Overview**
The `src` folder is structured to keep the project modular and maintainable. Each script focuses on a specific functionality, making it easy to reuse and debug.

---

## **File Descriptions**
Below is a list of the scripts included in this folder:

1. **`data_cleaning.py`**  
   - Contains functions for cleaning the dataset (e.g., handling missing values, removing outliers, and ensuring data consistency).
   - Example functions:
     - `clean_missing_values()`
     - `remove_outliers()`

2. **`data_validation.py`**  
   - Implements functions to validate the integrity of the dataset after cleaning.
   - Example functions:
     - `validate_numeric_columns()`
     - `check_consistency()`

3. **`visualization.py`**  
   - Includes functions for generating visualizations like bar charts and line graphs.
   - Example functions:
     - `plot_bar_chart()`
     - `plot_line_graph()`

4. **`statistical_analysis.py`**  
   - Provides utilities for computing summary statistics such as mean, median, and standard deviation.
   - Example functions:
     - `calculate_statistics()`
     - `generate_summary()`

---

## **Usage**
To use any script, import it into your Python code or notebook as needed. Below are examples of how to use these scripts:

### **Example 1: Data Cleaning**
```python
from scripts.data_cleaning import clean_missing_values

# Clean the dataset
cleaned_data = clean_missing_values(raw_data)
