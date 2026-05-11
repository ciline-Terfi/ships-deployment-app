import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- PAGE CONFIG ---
st.set_page_config(page_title="Lab 6: Ship Performance Tool", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #007bff; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚢 Voyage Performance Estimator")
st.write("Lab 6: Implementing Interactive Widgets for Operational Decision Making")

# --- SIDEBAR: INPUT WIDGETS ---
st.sidebar.header("Voyage Parameters")

ship_type = st.sidebar.selectbox("Select Vessel Type", 
    ['Oil Service Boat', 'Fishing Trawler', 'Container Ship', 'Tanker Ship'])

fuel_type = st.sidebar.radio("Fuel Type", ['HFO', 'Diesel'])

distance = st.sidebar.slider("Planned Distance (nautical miles)", 
    min_value=10, max_value=500, value=150)

weather = st.sidebar.select_slider("Expected Weather", 
    options=['Calm', 'Moderate', 'Stormy'])

# --- LOGIC: DYNAMIC CALCULATIONS ---
# Based on Lab 5 findings, we simulate the logic:
base_consumption = 30 if fuel_type == 'Diesel' else 35
weather_penalty = {'Calm': 1.0, 'Moderate': 1.2, 'Stormy': 1.6}

estimated_fuel = (distance * base_consumption / 10) * weather_penalty[weather]
estimated_co2 = estimated_fuel * 2.8  # Science-based conversion factor

# --- MAIN DISPLAY: METRICS ---
col1, col2 = st.columns(2)
with col1:
    st.metric("Estimated Fuel (Tons)", f"{estimated_fuel:.2f}")
with col2:
    st.metric("Estimated CO2 Impact", f"{estimated_co2:.2f}")

# --- VISUALIZATION: LIVE COMPARISON ---
st.divider()
st.subheader("Performance Context")

# Load dataset to compare user input with historical averages
df = pd.read_csv('/home/ciline/Téléchargements/ship_fuel_efficiency.csv')
avg_efficiency = df[df['ship_type'] == ship_type]['engine_efficiency'].mean()

st.write(f"The historical average efficiency for a **{ship_type}** is **{avg_efficiency:.2f}%**.")

# Plotting
fig, ax = plt.subplots(figsize=(8, 4))
sns.kdeplot(df[df['ship_type'] == ship_type]['engine_efficiency'], fill=True, color="blue", label="Historical Data")
plt.axvline(82, color='red', linestyle='--', label="Your Current Estimate") # Simulated estimate
plt.legend()
st.pyplot(fig)

if st.button("Generate Final Report"):
    st.success(f"Report generated for {ship_type} navigating {distance} miles in {weather} weather.")