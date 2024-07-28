import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(layout="wide", page_title="XSEED Player Performance Viewer")

# Title of the app
st.title("XSEED Player Performance Viewer.")

# Upload CSV file for stats
st.header("Upload CSV File for Stats")
uploaded_file = st.file_uploader("Choose a CSV file for the stats", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Display the dataframe
    st.write("Here is the CSV file of the stats of the player performance:")
    st.dataframe(df)
else:
    st.write("Please upload a CSV file to see the contents.")

# Divider
st.markdown("---")

# Upload CSV file for player performance data
st.header("Upload CSV File for Player Performance Data")
uploaded_performance_file = st.file_uploader("Choose a CSV file for player performance data", type="csv", key="performance_csv")

if uploaded_performance_file is not None:
    # Read the CSV file
    df_performance = pd.read_csv(uploaded_performance_file)

    # Display the dataframe
    st.write("Here is the CSV file of the player performance data:")
    st.dataframe(df_performance)
    
    # Check if 'gps_speed_mean_sm' exists in the dataframe
    default_y_column = 'gps_speed_mean_sm' if 'gps_speed_mean_sm' in df_performance.columns else df_performance.columns[0]
    
    # Select Y column to plot
    y_column = st.selectbox("Select the column to plot against 'gps_time'", df_performance.columns, index=df_performance.columns.get_loc(default_y_column))
    
    # Plotting with Plotly
    if y_column:
        st.write(f"Plotting 'gps_time' vs '{y_column}'")
        fig = px.line(df_performance, x='gps_time', y=y_column, title=f'gps_time vs {y_column}')
        st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Please upload a CSV file to see the contents.")
