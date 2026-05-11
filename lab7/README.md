

# Lab 7: Predictive Modeling with Simple Linear Regression

## 1. Project Overview

In Lab 7, we transition from descriptive analysis to **Predictive Analytics**. The objective is to construct a Supervised Machine Learning model that can accurately predict a vessel's **Fuel Consumption** based on its **Distance** traveled. This model serves as a foundational tool for maritime logistics and fuel budgeting.

## 2. Learning Objectives

* **Data Preprocessing:** Splitting a dataset into training and testing subsets to evaluate model generalization.
* **Supervised Learning:** Implementing the `LinearRegression` algorithm using the `scikit-learn` framework.
* **Model Interpretation:** Understanding the physical meaning of the **Slope (Coefficient)** and the **y-intercept**.
* **Performance Validation:** Applying statistical metrics such as **R-squared ($R^2$)** and **Mean Squared Error (MSE)** to judge model accuracy.

## 3. Mathematical Foundations

The model assumes a linear relationship between the input (Feature) and the output (Target):


$$Y = \beta_1 X + \beta_0 + \epsilon$$


Where:

* **$Y$:** Predicted Fuel Consumption.
* **$X$:** Distance (Nautical Miles).
* **$\beta_1$ (Coefficient):** The rate of fuel burn per mile.
* **$\beta_0$ (Intercept):** The estimated fuel used for starting/idling (baseline consumption).
* **$\epsilon$:** Residual error (variance not explained by distance).

## 4. Implementation Details

### Step 1: Feature Selection

We selected `distance` as the independent variable ($X$) because earlier Exploratory Data Analysis (EDA) in Lab 5 showed a strong linear correlation with `fuel_consumption` ($y$).

### Step 2: The 80/20 Split

To ensure the model is not just "memorizing" the data (overfitting), we partitioned the data:

* **Training Set (80%):** Used to teach the model the relationship between variables.
* **Testing Set (20%):** Used to simulate "new" data and check prediction accuracy.

### Step 3: Visualization

A regression plot was generated to visually inspect the "Line of Best Fit." This allows us to see how well the red prediction line follows the trend of the blue data points.

## 5. Statistical Results & Interpretation

Based on the `ship_fuel_efficiency.csv` dataset, the model yielded the following:

* **Coefficient (~42.57):** For every 1 nautical mile traveled, the ship consumes approximately 42.57 tons of fuel.
* **R-squared (~0.91):** Approximately 91% of the variation in fuel consumption can be explained by distance alone. This indicates a **highly reliable model**.
* **MSE:** Measures the average squared difference between estimated values and the actual value.

## 6. Conclusion

Lab 7 successfully demonstrates the power of Simple Linear Regression in maritime operations. While distance is the primary driver of fuel use, the 9% of unexplained variance ($R^2 = 0.91$) suggests that secondary features like **Weather Conditions** and **Ship Type** are necessary for a more complex "Multiple Linear Regression" model.
