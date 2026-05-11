Lab 6: Interactive Operational Dashboards with Streamlit
1. Executive Summary

The goal of Lab 6 is the transition from Static Data Analysis to Interactive Application Development. Using the ship_fuel_efficiency.csv dataset, we have developed a "Voyage Performance Estimator." This tool allows maritime operators to input real-time parameters (distance, weather, fuel type) and receive instant projections on fuel consumption and CO2 impact, compared against historical baseline distributions.
2. Key Objectives

    UI/UX Design: Implementing a clean, professional sidebar for user control using st.sidebar.

    Dynamic State Management: Using Streamlit's reactive framework to update metrics and visualizations instantly as user inputs change.

    Operational Logic: Translating historical data patterns (fuel consumption per mile) into a predictive heuristic for future voyage planning.

    Resource Optimization: Implementing @st.cache_data to ensure the application remains performant even with repeated user interactions.

3. Application Components
A. Parameter Input (Sidebar)

We utilize a combination of widgets to capture the full context of a maritime voyage:

    SelectBox: Automatically populated with unique vessel types from the dataset to ensure data integrity.

    Radio Buttons: For selecting fuel categories (HFO vs. Diesel).

    Slider: For precise distance modeling (10 to 500 nautical miles).

    Select Slider: An intuitive way to model environmental difficulty (Calm, Moderate, Stormy).

B. Predictive Engine

The application calculates estimates based on the average performance of the selected vessel type:

    Fuel Estimation: Derived from historical fuel_consumption / distance ratios.

    Weather Penalty: A multiplier applied to simulate increased drag and reduced efficiency in stormy conditions.

    Environmental Impact: CO2 projection calculated via standard maritime conversion factors.

C. Comparative Visualization

A Kernel Density Estimate (KDE) Plot is generated to show where the current ship type typically operates in terms of engine_efficiency. A vertical dashed line marks the historical average, allowing the user to contextualize their planned voyage within the fleet's historical performance.
4. Technical Stack

    Framework: Streamlit (v1.30.0+)

    Data Processing: Pandas

    Visualization: Seaborn, Matplotlib

    Environment: Kali Linux / Virtual Environment (lab_env)

5. Deployment & Execution

To preview the operational tool, navigate to the laboratory directory and execute the following command:
Bash

# Ensure the virtual environment is active
source ~/Data-Analysis-ENSTA/ciline-terfi/lab6/lab_env/bin/activate

# Launch the Streamlit server
streamlit run streamlitexe.py

6. Project Findings

    User Engagement: Interactivity allows for faster "what-if" analysis compared to static Jupyter Notebooks.

    Data Reactivity: By using unique() functions for filters, the app is "future-proof"—adding new ship types to the CSV will automatically update the UI without code changes.

    Efficiency Insight: The KDE plots reveal that while most engines operate at peak efficiency, "Stormy" conditions create significant outliers that the estimator correctly accounts for.