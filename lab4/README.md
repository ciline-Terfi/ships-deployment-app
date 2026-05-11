Lab 5: Exploratory Data Analysis (EDA) – Naval Forces Dataset
1. Project Overview

This laboratory focuses on performing a comprehensive Exploratory Data Analysis (EDA) on a dataset of global naval strengths. The objective is to apply data cleaning, statistical analysis, and visualization techniques to understand the distribution of maritime power across different nations and identify correlations between various ship classes.
2. Objectives

    Perform data inspection and quality checks (handling null values and data types).

    Generate descriptive statistics to understand the scale of naval equipment.

    Apply Feature Engineering to create categorical groups from numerical data (e.g., classifying fleet sizes).

    Visualize data using Matplotlib and Seaborn (Pie charts, Histograms, Boxplots, and Heatmaps).

    Identify outliers and correlations within the global fleet.

3. Dataset Description

The dataset naval_forces.csv contains information on the naval equipment of various countries, including:

    Nation: The name of the country.

    Total: Total number of naval assets.

    Aircraft Carriers, Destroyers, Frigates, Corvettes, Submarines: Specific counts for each vessel class.

4. Technical Stack

    Language: Python 3.x

    Environment: Kali Linux / Jupyter Notebook

    Libraries: * pandas: For data manipulation and CSV handling.

        seaborn & matplotlib: For advanced statistical data visualization.

        os: For file system management and error handling.

5. EDA Workflow
Phase 1: Data Audit

Checking for missing values and verifying the structure using .info() and .describe(). This ensures the data is clean before visualization.
Phase 2: Univariate Analysis

Analyzing single variables to see distributions.

    Histogram: Visualizing the skewness of the "Total" fleet size.

    Pie Chart: Breaking down the composition of a single nation's navy.

Phase 3: Bivariate & Categorical Analysis

Exploring relationships between two variables.

    Countplots: Using custom logic (e.g., Large_Sub_Fleet) to categorize nations based on equipment thresholds.

    Bar Charts: Comparing the Top 10 naval powers globally.

Phase 4: Multivariate Analysis

    Heatmap: Generating a correlation matrix to see how the possession of one ship type (like Destroyers) relates to others (like Frigates).

    Boxplots: Identifying statistical outliers (nations with disproportionately large fleets).

6. Key Findings (Sample)

    Distribution: Naval power is highly skewed, with a few "superpower" nations acting as statistical outliers.

    Composition: Most navies prioritize smaller, versatile vessels (Frigates/Corvettes) over capital ships (Carriers).

    Correlation: There is a strong positive correlation between a nation's total fleet size and its number of submarines.