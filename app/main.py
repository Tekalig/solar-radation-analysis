import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
# Import cleaning and analysis functions from utils.py
from app.utils import clean_data, time_series_analysis, correlation_analysis, plot_histograms

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current directory of this script
data_dir = os.path.join(current_dir, "../../src/data/")  # Adjust the path



# Set Streamlit page configuration
st.set_page_config(
    page_title="MoonLight Solar Dashboard",
    layout="wide",
    initial_sidebar_state="auto"
)

# Title
st.title("☀️ MoonLight Energy Solutions: Solar Data Analysis Dashboard ☀️")
st.write("""
This dashboard provides insights into solar radiation data across three regions:
- Togo
- Sierra Leone
- Benin

Explore interactive visualizations based on historical solar radiation, wind conditions, temperature effects, and other environmental factors.
""")

# Sidebar with Dataset Selection
st.sidebar.header("Dataset Selector")
dataset_option = st.sidebar.selectbox(
    "Choose a dataset:",
    ["Togo", "Sierra Leone", "Benin"]
)

# Load data depending on the selected option
dataset_files = {
    "Togo": os.path.join(data_dir, "togo-dapaong_qc.csv"),
    "Sierra Leone": os.path.join(data_dir, "sierraleone-bumbuna.csv"),
    "Benin": os.path.join(data_dir, "benin-malanville.csv")
}

# Read the selected CSV
data = pd.read_csv(dataset_files[dataset_option])

# Cleaning
st.sidebar.write("Processing and Cleaning Data...")
data_cleaned = clean_data(data)

# Tabs for visualization categories
tab1, tab2, tab3, tab4 = st.tabs(["Time Series Analysis", "Correlation Analysis", "Histograms", "Dashboard Insights"])


# Time Series Analysis
with tab1:
    st.header("📊 Time Series Analysis")
    time_series_var = st.selectbox(
        "Select variable to plot over time:",
        ["GHI", "DNI", "DHI", "Tamb"]
    )
    fig, ax = plt.subplots()
    data_cleaned['Timestamp'] = pd.to_datetime(data_cleaned['Timestamp'])
    ax.plot(data_cleaned['Timestamp'], data_cleaned[time_series_var], label=time_series_var)
    ax.set_title(f"{time_series_var} trends over time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Values")
    st.pyplot(fig)

# Correlation Analysis
with tab2:
    st.header("🔗 Correlation Analysis")
    corr_vars = st.multiselect(
        "Select variables for correlation analysis:",
        ["GHI", "DNI", "DHI", "TModA", "TModB", "RH"]
    )
    if len(corr_vars) > 1:
        corr_matrix = correlation_analysis(data_cleaned, corr_vars)
        st.write(corr_matrix)
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
        st.pyplot(plt)
    else:
        st.warning("Select at least 2 variables to compute correlation.")

# Histogram visualization
with tab3:
    st.header("📊 Histograms")
    hist_var = st.selectbox(
        "Select variable to visualize:",
        ["GHI", "DNI", "DHI", "WS", "Tamb"]
    )
    fig, ax = plt.subplots()
    plot_histograms(data_cleaned, hist_var, ax)

# Insights Panel
with tab4:
    st.header("🚀 Dashboard Insights")
    st.write("""
    Use this section to gather insights about anomalies, outliers, and environmental trends.
    This will assist in identifying strategic regions for solar installation.
    """)

st.sidebar.success("Data cleaned and ready for visualization!")
