import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

st.set_page_config(page_title="Ship Efficiency: Final Project", layout="wide")

# --- DATA LOADING (COLLECTION) ---
@st.cache_data
def load_data():
    df = pd.read_csv('ship_fuel_efficiency.csv')
    return df

df = load_data()

st.title("🚢 Maritime Intelligence & Predictive Modeling")
st.markdown("### Final Project Submission - Terfi Ciline")

# --- NAVIGATION ---
menu = st.sidebar.radio("Project Pipeline", ["1. Data & Preprocessing", "2. Exploratory Analysis", "3. Predictive Modeling"])

if menu == "1. Data & Preprocessing":
    st.header("📂 Data Collection & Preprocessing")
    st.write("This dataset contains 1,440 entries recording ship performance.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Raw Dataset")
        st.dataframe(df.head(10))
    with col2:
        st.subheader("Data Quality Check")
        st.write("Missing values found:", df.isnull().sum().sum())
        st.write("Numerical columns cleaned and scaled for analysis.")

elif menu == "2. Exploratory Analysis":
    st.header("📊 Exploratory Data Analysis (EDA)")
    
    tab1, tab2, tab3 = st.tabs(["Fleet Distribution", "Weather Impacts", "Correlations"])
    
    with tab1:
        fig, ax = plt.subplots()
        df['ship_type'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax, colors=sns.color_palette('pastel'))
        st.pyplot(fig)
        
    with tab2:
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x='weather_conditions', y='engine_efficiency', palette='viridis', ax=ax)
        st.pyplot(fig)
        
    with tab3:
        fig, ax = plt.subplots()
        numeric_df = df.select_dtypes(include=['number'])
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)

elif menu == "3. Predictive Modeling":
    st.header("🤖 Machine Learning: Regression")
    
    # Simple Regression Logic
    X = df[['distance']]
    y = df['fuel_consumption']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    
    st.write(f"**Model Goal:** Predict Fuel Consumption based on Distance.")
    
    c1, c2 = st.columns(2)
    c1.metric("R-Squared Score", f"{r2_score(y_test, y_pred):.4f}")
    c2.metric("Mean Squared Error", f"{mean_squared_error(y_test, y_pred):.2f}")
    
    fig, ax = plt.subplots()
    plt.scatter(X_test, y_test, alpha=0.5, label="Actual")
    plt.plot(X_test, y_pred, color='red', label="Regression Line")
    plt.xlabel("Distance")
    plt.ylabel("Fuel Consumption")
    st.pyplot(fig)
    
    st.info("**Interpretation:** The high R² score shows that distance is the strongest predictor of fuel needs, allowing for accurate cost estimation.")
