import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

def plot_temperature_vs_conversion(data):
    fig = px.scatter(
        data_frame=data,
        x='Temperature (°C)', 
        y='Conversion (%)',
        color='Reactor Type',
        title='Temperature vs. Conversion',
        labels={'Temperature (°C)': 'Temperature (°C)', 'Conversion (%)': 'Conversion (%)'}
    )
    fig.update_traces(marker=dict(size=12))
    st.plotly_chart(fig)

def plot_catalyst_vs_reaction_rate(data):
    fig = px.scatter(
        data_frame=data,
        x='Catalyst Loading (%)', 
        y='Reaction Rate (mol/s)',
        color='Reactor Type',
        title='Catalyst Loading vs. Reaction Rate',
        labels={'Catalyst Loading (%)': 'Catalyst Loading (%)', 'Reaction Rate (mol/s)': 'Reaction Rate (mol/s)'}
    )
    fig.update_traces(marker=dict(size=12))
    st.plotly_chart(fig)

def plot_correlation_matrix(data):
    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_data.corr()

    # Create a heatmap using Plotly
    fig = go.Figure(data=go.Heatmap(
        z=correlation_matrix.values,
        x=correlation_matrix.columns,
        y=correlation_matrix.columns,
        colorscale='Viridis',
        colorbar=dict(title='Correlation Coefficient')
    ))

    fig.update_layout(
        title="Correlation Matrix",
        xaxis_title="Parameters",
        yaxis_title="Parameters",
        height=600
    )

    st.plotly_chart(fig)

def display_comparison_graphs(data, reactor1, reactor2):
    data_r1 = data[data['Reactor Type'] == reactor1]
    data_r2 = data[data['Reactor Type'] == reactor2]

    st.write(f"Comparing {reactor1} with {reactor2}")

    # First comparison: Temperature vs Conversion
    fig1 = px.scatter(
        data_frame=pd.concat([data_r1, data_r2]),
        x='Temperature (°C)', 
        y='Conversion (%)',
        color='Reactor Type',
        title=f'{reactor1} vs. {reactor2}: Temperature vs. Conversion',
        labels={'Temperature (°C)': 'Temperature (°C)', 'Conversion (%)': 'Conversion (%)'}
    )
    fig1.update_traces(marker=dict(size=12))
    st.plotly_chart(fig1)

    # Second comparison: Catalyst Loading vs Reaction Rate
    fig2 = px.scatter(
        data_frame=pd.concat([data_r1, data_r2]),
        x='Catalyst Loading (%)', 
        y='Reaction Rate (mol/s)',
        color='Reactor Type',
        title=f'{reactor1} vs. {reactor2}: Catalyst Loading vs. Reaction Rate',
        labels={'Catalyst Loading (%)': 'Catalyst Loading (%)', 'Reaction Rate (mol/s)': 'Reaction Rate (mol/s)'}
    )
    fig2.update_traces(marker=dict(size=12))
    st.plotly_chart(fig2)
