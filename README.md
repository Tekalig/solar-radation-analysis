# Solar Analysis Project

## About
This project analyzes solar data to find good locations for solar panels. We look at weather and solar measurements to make smart investment decisions.

## Data We Use
We collect:
- Solar measurements 
- Weather data
- Panel readings
- Cleaning records

### What's in the Data
- Time and date
- Solar readings:
  - Ground sunlight (GHI)
  - Direct sunlight (DNI)
  - Scattered light (DHI)
- Panel info:
  - Power output
  - Temperature
- Weather:
  - Temperature
  - Humidity
  - Wind speed
  - Wind direction
  - Air pressure
  - Rain
- Other:
  - When panels were cleaned
  - Notes

## Getting Started
1. Get the code:
    ```bash
    git clone https://github.com/solar-project/analysis.git
    ```
2. Install tools:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up:
    ```bash
    python setup.py
    ```
4. Run:
    ```bash
    python start.py
    ```
