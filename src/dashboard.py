import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from data_loader import load_and_clean_data
from visualizations import (
    plot_temperature_vs_conversion,
    plot_catalyst_vs_reaction_rate,
    plot_correlation_matrix,
    display_comparison_graphs
)

# Load the reactor performance data
data = load_and_clean_data('data/reactor_performance.csv')

# Streamlit app title
st.title("Reactor Performance Analysis Dashboard")
st.markdown("""
    This dashboard visualizes the performance of Batch, CSTR, and PFR reactors under different operating conditions.
""")

# Sidebar for selecting reactor type
reactor_type = st.sidebar.selectbox('Select Reactor Type', ['All', 'Batch', 'CSTR', 'PFR'])

# Filter sliders for temperature and pressure
min_temp, max_temp = st.sidebar.slider("Select Temperature Range (°C)", int(data['Temperature (°C)'].min()), int(data['Temperature (°C)'].max()), (100, 150))
min_pressure, max_pressure = st.sidebar.slider("Select Pressure Range (bar)", float(data['Pressure (bar)'].min()), float(data['Pressure (bar)'].max()), (1.0, 2.0))

# Filter data based on reactor type and user-defined ranges
filtered_data = data[(data['Temperature (°C)'] >= min_temp) & (data['Temperature (°C)'] <= max_temp) &
                     (data['Pressure (bar)'] >= min_pressure) & (data['Pressure (bar)'] <= max_pressure)]

if reactor_type != 'All':
    filtered_data = filtered_data[filtered_data['Reactor Type'] == reactor_type]

# Display filtered data
st.write(f"Data for {reactor_type} Reactor")
st.dataframe(filtered_data)

# Display statistical summary of filtered data
st.subheader("Statistical Summary")
st.write(filtered_data.describe())

# Visualization 1: Temperature vs. Conversion
st.subheader(f"Temperature vs. Conversion for {reactor_type} Reactor")
plot_temperature_vs_conversion(filtered_data)

# Visualization 2: Catalyst Loading vs. Reaction Rate
st.subheader(f"Catalyst Loading vs. Reaction Rate for {reactor_type} Reactor")
plot_catalyst_vs_reaction_rate(filtered_data)

# Visualization 3: Correlation Matrix
st.subheader("Correlation Matrix")
plot_correlation_matrix(filtered_data)

# Comparison Tool: Select two reactor types for side-by-side comparison
st.subheader("Reactor Comparison")
reactor1 = st.selectbox('Select First Reactor Type', ['Batch', 'CSTR', 'PFR'])
reactor2 = st.selectbox('Select Second Reactor Type', ['Batch', 'CSTR', 'PFR'])
display_comparison_graphs(data, reactor1, reactor2)

# Download button for filtered data
def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.
    """
    if isinstance(object_to_download, pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=False)

    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{download_link_text}</a>'

st.markdown(download_link(filtered_data, 'filtered_data.csv', 'Download Filtered Data'), unsafe_allow_html=True)

# Add tooltips and help sections
st.markdown("""
    **Note**: Hover over data points to see more details. The correlation matrix helps in understanding the relationships between variables.
""")
