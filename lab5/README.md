Lab 5: Exploratory Data Analysis (EDA) – Ship Fuel Efficiency
1. Project Overview

This laboratory focuses on the application of Exploratory Data Analysis (EDA) techniques to evaluate maritime operational data. Using a dataset of 1,440 ship voyages, this project explores the relationships between distance, weather conditions, fuel types, and environmental impact (CO2 emissions).
2. Objectives

    Data Quality Assessment: Identify and handle missing values, and verify data types.

    Univariate Analysis: Understand the distribution of individual variables like engine efficiency and fuel consumption.

    Categorical Investigation: Analyze the frequency of weather conditions and the diversity of the fleet.

    Bivariate/Multivariate Analysis: Discover how distance and weather correlate with total fuel consumption and CO2 output.

    Outlier Detection: Use statistical visualization to identify anomalous voyages.

3. Dataset Specification

The ship_fuel_efficiency.csv file contains the following key features:

    Ship_id & Ship_type: Identification and classification (e.g., Tanker, Oil Service Boat).

    Route_id & Month: Spatial and temporal context of the voyage.

    Distance: Total nautical miles traveled.

    Fuel_type: Type of fuel used (HFO or Diesel).

    Fuel_consumption: Amount of fuel used (metric tons).

    CO2_emissions: Measured carbon footprint.

    Weather_conditions: Environmental state (Calm, Moderate, Stormy).

    Engine_efficiency: Percentage of engine performance.

4. Technical Requirements

    Language: Python 3.13+

    Core Libraries:

        pandas: Data manipulation and frame handling.

        seaborn: Statistical data visualization.

        matplotlib: Plot customization and rendering.

    Tools: VS Code / Kali Linux Terminal / Streamlit (for optional deployment).

5. Implementation Workflow
Phase 1: Structural Audit

We begin by checking the "shape" of the data. This mirrors the initial steps of identifying non-null counts and basic statistics to ensure the data is reliable for modeling.
Phase 2: Distribution & Composition

    Pie Charts: Used to visualize the proportion of different ship types within the dataset.

    Histograms: Used to visualize engine_efficiency. We look for a "Normal Distribution" to see if most engines perform within a standard range.

Phase 3: Performance & Environmental Impact

    Bar Charts: Comparing average fuel consumption across different ship types.

    Boxplots: Crucial for identifying "Outliers." For example, we check if certain voyages had unusually high CO2 emissions due to engine failure or extreme weather.

Shutterstock

    Explore 

Phase 4: Correlation Matrix

The final step is the Heatmap. This reveals the mathematical relationship between variables.

    Key Hypothesis: We expect a high positive correlation between distance and fuel_consumption.
6.Preliminary Observations

    Environmental Impact: CO2 emissions scale linearly with fuel consumption, confirming the validity of the data.

    Operational Trends: Weather conditions significantly impact engine efficiency, with "Stormy" conditions showing a wider variance in performance.

    Fleet Diversity: The fleet is comprised of various vessel types, each showing distinct consumption profiles.