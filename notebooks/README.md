# Solar Energy Potential Analysis

This project analyzes solar energy potential across three regions (Togo, Ser, and Benin) using key solar irradiance metrics and temperature data to determine the most suitable region for solar energy investments.

---

## **Table of Contents**
1. [Overview](#overview)
2. [Dataset Description](#dataset-description)
3. [Key Metrics](#key-metrics)
4. [Setup Instructions](#setup-instructions)
5. [Running the Notebook](#running-the-notebook)
6. [Results and Insights](#results-and-insights)

---

## **Overview**
The analysis evaluates solar irradiance metrics:
- **Global Horizontal Irradiance (GHI)**
- **Direct Normal Irradiance (DNI)**
- **Diffuse Horizontal Irradiance (DHI)**
- **Ambient Temperature (Tamb)**

The objective is to recommend the most suitable region for solar energy projects by analyzing the data and visualizing the results.

---

## **Dataset Description**
The dataset contains solar irradiance and temperature data for Togo, Ser, and Benin. Key columns include:
- `Region`
- `GHI` (Global Horizontal Irradiance)
- `DNI` (Direct Normal Irradiance)
- `DHI` (Diffuse Horizontal Irradiance)
- `Tamb` (Temperature)

Data preprocessing steps:
1. Cleaning missing values.
2. Removing outliers.
3. Calculating summary statistics.

---

## **Key Metrics**
- **Mean GHI, DNI, DHI**: Indicates potential solar energy yield.
- **Standard Deviation**: Measures variability in solar conditions.
- **Temperature**: Impacts panel efficiency but is factored into the recommendation.

---

## **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   
4. Running the Notebook
   ```bash
      Open the solar_energy_analysis.ipynb notebook in Jupyter Notebook.
      Run each cell sequentially to:
      Load the dataset.
      Preprocess the data.
      Generate statistical summaries and visualizations.
      View the final recommendation and insights.
      Results and Insights
5. The analysis concludes that:
   Benin is the most favorable region for solar energy investments due to its superior solar irradiance metrics.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contact**
For questions or suggestions, please contact:

Name: Tekalign Mesfin
Email: [your_email@example.com]
