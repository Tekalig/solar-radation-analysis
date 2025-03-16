# Scripts Folder

This folder is responsible for importing and running code from the `src` folder in one place. It contains scripts for data preprocessing, analysis, and visualization. Each script is designed to perform specific tasks to ensure the data is clean, well-analyzed, and the results are effectively communicated.

### **Contents**
- `data_preprocessing.py`: Cleans and prepares the dataset for analysis.
- `exploratory_data_analysis.py`: Performs initial data exploration and visualization.
- `results_visualization.py`: Generates plots and charts to visualize the analysis results.

These scripts work together to provide a comprehensive analysis of solar irradiance data, helping to identify the best regions for solar energy projects.


## **Overview**
The analysis evaluates solar irradiance metrics:
- **Global Horizontal Irradiance (GHI)**
- **Direct Normal Irradiance (DNI)**
- **Diffuse Horizontal Irradiance (DHI)**
- **Ambient Temperature (Tamb)**

The objective is to recommend the most suitable region for solar energy projects by analyzing the data and visualizing the results.

---

## **Dataset Description**
The dataset contains solar irradiance and temperature data for Togo, Benin, and Ghana. Key columns include:
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
   git clone https://github.com/Tekalig/solar-radation-analysis.git
   cd solar-radation-analysis
  ```

2. Install dependencies:
```bash
   pip install -r requirements.txt
```


3. Run the analysis script:
```bash
   python scripts/exploratory_data_analysis.py
   ```   

4. The analysis concludes that:
   Benin is the most favorable region for solar energy investments due to its superior solar irradiance metrics.

**License**
This project is licensed under the MIT License. See the LICENSE file for more details.

**Contact**
For questions or suggestions, please contact:

Name: Tekalign Mesfin
Email: [tekahazi06@gmail.com]
