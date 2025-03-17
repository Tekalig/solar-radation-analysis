import pytest 
import pandas as pd
from src.histograms import plot_histograms

df = pd.DataFrame({
    'GHI': [100, 200, 300, 400, 500],
    'DNI': [50, 100, 150, 200, 250],
    'DHI': [10, 20, 30, 40, 50],
    'WS': [5, 10, 15, 20, 25],
    'Tamb': [20, 25, 30, 35, 40],
    'TModA': [22, 27, 32, 37, 42],
    'TModB': [24, 29, 34, 39, 44]
})

def test_plot_histograms():
    plot_histograms(df, "Togo")
    assert True
