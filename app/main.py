import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Import cleaning and analysis functions
from utils import (
    clean_data,
    time_series_analysis,
    correlation_analysis,
    plot_histograms,
)

# Set Streamlit page configuration
st.set_page_config(
    page_title="MoonLight Solar Dashboard", layout="wide", initial_sidebar_state="auto"
)

# Title
st.title("☀️ MoonLight Energy Solutions: Solar Data Analysis Dashboard ☀️")
st.write(
    """
This dashboard provides insights into solar radiation data across three regions:
- Togo
- Sierra Leone
- Benin

Explore interactive visualizations based on historical solar radiation, wind conditions, temperature effects, and other environmental factors.
"""
)

# Sidebar with Dataset Selection
st.sidebar.header("Dataset Selector")
dataset_option = st.sidebar.selectbox(
    "Choose a dataset:", ["Togo", "Sierra Leone", "Benin"]
)

dataset_files = {
    "Togo": os.path.join(os.getcwd(), "data/processed/cleaned_togo.csv"),
    "Sierra Leone": os.path.join(os.getcwd(), "data/processed/cleaned_sierraleone.csv"),
    "Benin": os.path.join(os.getcwd(), "data/processed/cleaned_benin.csv"),
}

# Load the data
try:
    st.sidebar.write("Loading data...")
    data = pd.read_csv(dataset_files[dataset_option])
except FileNotFoundError as e:
    st.error(f"File not found: {e}")
    st.stop()

# Cleaning
st.sidebar.write("Processing and Cleaning Data...")
data_cleaned = clean_data(data)

# Tabs for visualization categories
tab1, tab2, tab3 = st.tabs(
    ["Time Series Analysis", "Correlation Analysis", "Histograms"]
)

# Time Series Analysis
with tab1:
    st.header("📊 Time Series Analysis")
    time_series_var = st.selectbox(
        "Select variable to plot over time:", ["GHI", "DNI", "DHI", "Tamb"]
    )
    fig = time_series_analysis(data_cleaned, time_series_var)
    st.pyplot(fig)

# Correlation Analysis
with tab2:
    st.header("🔗 Correlation Analysis")
    corr_vars = st.multiselect(
        "Select variables for correlation analysis:",
        ["GHI", "DNI", "DHI", "TModA", "TModB", "RH"],
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
        "Select variable to visualize:", ["GHI", "DNI", "DHI", "WS", "Tamb"]
    )
    fig, ax = plt.subplots()
    plot_histograms(data_cleaned, hist_var, ax)
    st.pyplot(fig)

st.sidebar.success("Data cleaned and ready for visualization!")
