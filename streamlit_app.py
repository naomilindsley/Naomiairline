import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import seaborn as sns
import numpy as np

# Set the page configuration
st.set_page_config(page_title="Airline Satisfaction Prediction", page_icon="✈️")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a Page", ["Home", "Data Overview", "Exploratory Data Analysis", "Extras"])

# Data Preparation
uploaded_file = st.sidebar.file_uploader("Upload your Airline Excel file", type=["xlsx", "xls"])
if uploaded_file is not None:
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.sidebar.error("Error: Unable to read the uploaded file. Please upload a valid Excel file.")
else:
    df = None

# Home Page
if page == "Home":
    st.title("Airline Satisfaction Prediction Project ✈️")
    st.subheader("Welcome!")
    st.write(
        """
        The dataset used in this project is the "Airline Passenger Satisfaction" dataset, which can be downloaded from Kaggle. 
        The dataset contains information about airline passengers, including features such as flight distance, seat comfort, inflight entertainment, and more.
        """
    )
    st.subheader("Upload and Display an Image")
    uploaded_image = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption='Uploaded Image', use_column_width=True)

# Data Overview Page
elif page == "Data Overview" and df is not None:
    st.title("Data Overview")
    st.subheader("About the Dataset")
    st.write(
        """
        This dataset includes information about airline passengers, such as:
        - **Gender**: Gender of the passengers (Female, Male)
        - **Customer Type**: The customer type (Loyal customer, disloyal customer)
        - **Age**: The actual age of the passengers
        - **Type of Travel**: Purpose of the flight of the passengers (Personal Travel, Business Travel)
        - **Class**: Travel class in the plane of the passengers (Business, Eco, Eco Plus)
        - **Flight distance**: The flight distance of this journey
        - **Inflight wifi service**: Satisfaction level of the inflight wifi service (0: Not Applicable; 1-5)
        - **Departure/Arrival time convenient**: Satisfaction level of Departure/Arrival time convenience
        - **Ease of Online booking**: Satisfaction level of online booking
        - **Gate location**: Satisfaction level of Gate location
        - **Food and drink**: Satisfaction level of Food and drink
        - **Online boarding**: Satisfaction level of online boarding
        - **Seat comfort**: Satisfaction level of Seat comfort
        - **Inflight entertainment**: Satisfaction level of inflight entertainment
        - **On-board service**: Satisfaction level of On-board service
        - **Leg room service**: Satisfaction level of Leg room service
        - **Baggage handling**: Satisfaction level of baggage handling
        - **Check-in service**: Satisfaction level of Check-in service
        - **Inflight service**: Satisfaction level of inflight service
        - **Cleanliness**: Satisfaction level of Cleanliness
        - **Departure Delay in Minutes**: Minutes delayed when departure
        - **Arrival Delay in Minutes**: Minutes delayed when Arrival
        - **Satisfaction**: Airline satisfaction level (Satisfaction, neutral or dissatisfaction)
        """
    )
    st.write("### Preview of the Dataset:")
    st.dataframe(df.head())
    st.write("### Summary Statistics:")
    st.write(df.describe())

# Exploratory Data Analysis (EDA) Page
elif page == "Exploratory Data Analysis" and df is not None:
    st.title("Exploratory Data Analysis 📊")

    # Numeric and Categorical Columns
    num_cols = df.select_dtypes(include=["number"]).columns.tolist()
    obj_cols = df.select_dtypes(include=["object"]).columns.tolist()

    # Select Visualization Type
    st.subheader("Select a Visualization:")
    eda_type = st.multiselect("Choose visualization(s):", ["Histogram", "Box Plot", "Bar Plot"])

    # Histogram
    if "Histogram" in eda_type:
        st.subheader("Histogram")
        selected_col = st.selectbox("Select a numerical column:", num_cols)
        if selected_col:
            st.plotly_chart(px.histogram(df, x=selected_col, title=f"Histogram of {selected_col}"))

    # Box Plot
    if "Box Plot" in eda_type:
        st.subheader("Box Plot")
        y_col = st.selectbox("Select a column for Box Plot (y-axis):", num_cols)
        x_col = st.selectbox("Select a column for Box Plot (x-axis):", obj_cols)
        if y_col and x_col:
            st.plotly_chart(px.box(df, x=x_col, y=y_col, title=f"Box Plot: {y_col} vs {x_col}", color=x_col))

    # Bar Plot
    if "Bar Plot" in eda_type:
        st.subheader("Bar Plot")
        x_col = st.selectbox("Select x-axis (categorical):", obj_cols, key="bar_x")
        y_col = st.selectbox("Select y-axis (numerical):", num_cols, key="bar_y")
        if x_col and y_col:
            st.plotly_chart(px.bar(df, x=x_col, y=y_col, title=f"Bar Plot: {y_col} by {x_col}", color=x_col))

# Extras Page
elif page == "Extras":
    st.title("Useful Information")

    st.subheader("Airline Demand-Supply Imbalance is Good for Revenue, Tough on Customer Experience, Says J.D. Power")
    st.write(
        """
        ROY, Mich.: 10 May 2023 — A combination of soaring demand, limited supply, and surging airfares have helped airlines book record revenues during the past two quarters, but this golden age of enhanced revenues is coming at the expense of customer satisfaction. According to the J.D. Power 2023 North America Airline Satisfaction Study, customer satisfaction with major airlines is down significantly for a second consecutive year, introducing the risk of possible brand damage if the current pattern of price hikes, staffing shortages, and reduced routes continues.

        “If yield management were the only metric airlines needed to be successful in the long term, this would be a banner year for the industry because they are operating at peak economic efficiency,” said Michael Taylor, travel intelligence lead at J.D. Power. “From the customer perspective, however, that means planes are crowded, tickets are expensive, and flight availability is constrained. While these drawbacks have not yet put a dent in leisure travel demand, if this trend continues, travelers will reach a breaking point and some airline brands may be
::contentReference[oaicite:0]{index=0}
 
