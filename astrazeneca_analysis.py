import streamlit as st
import pandas as pd


# Create a DataFrame
astrazeneca_df = pd.read_csv("astrazeneca_data.csv")

# Streamlit app
st.title("Medicine Ingredients Analysis")

# Sidebar for user input
selected_year = st.sidebar.selectbox("Select Year", astrazeneca_df['Year'].unique())
selected_route = st.sidebar.selectbox("Select Route", astrazeneca_df['route'].unique())

# Filter the data based on user input
filtered_data = astrazeneca_df[(astrazeneca_df['Year'] == selected_year) & (astrazeneca_df['route'] == selected_route)]
average_ingredients = filtered_data['Number_Ingredients'].mean()

# Display results
st.write(f"Average Ingredients in {selected_route} medicines for {selected_year}: {average_ingredients:.2f}")
