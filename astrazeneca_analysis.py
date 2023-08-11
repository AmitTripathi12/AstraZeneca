import streamlit as st
import pandas as pd


# Create a DataFrame
astrazeneca_df = pd.read_csv("astrazeneca_data.csv")

# Streamlit app
st.title("Medicine Ingredients Analysis per year per route")

# Sidebar for user input
selected_year = st.sidebar.selectbox("Select Year", astrazeneca_df['Year'].unique())
selected_route = st.sidebar.selectbox("Select Route", astrazeneca_df['route'].unique())

# Filter the data based on user input
filtered_data_route = astrazeneca_df[(astrazeneca_df['Year'] == selected_year) & (astrazeneca_df['route'] == selected_route)]
average_ingredients_route = filtered_data_route['Number_Ingredients'].mean()

filtered_data_year = astrazeneca_df[astrazeneca_df['Year'] == selected_year]
average_ingredients_year = filtered_data_year['Number_Ingredients'].mean()

