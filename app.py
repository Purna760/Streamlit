import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# App configuration
st.set_page_config(
    page_title="My Mobile App",
    page_icon="📱",
    layout="centered"
)

# Title and description
st.title("📱 My Streamlit Mobile App")
st.write("This app was created and deployed entirely from a mobile phone!")

# Sidebar
st.sidebar.header("Navigation")
menu = st.sidebar.selectbox("Choose a section", 
    ["Home", "Data Analysis", "About"])

if menu == "Home":
    st.header("Welcome! 👋")
    
    # User input
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hello, {name}! 👋")
    
    # Slider example
    age = st.slider("Select your age", 0, 100, 25)
    st.write(f"You selected: {age} years")
    
    # Button example
    if st.button("Click me!"):
        st.balloons()
        st.success("You clicked the button! 🎉")

elif menu == "Data Analysis":
    st.header("Data Analysis 📊")
    
    # Generate sample data
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100)
    })
    
    # Display data
    st.subheader("Sample Data")
    st.dataframe(data.head())
    
    # Chart
    st.subheader("Scatter Plot")
    st.scatter_chart(data, x='x', y='y', color='category')
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(data))
    with col2:
        st.metric("Unique Categories", data['category'].nunique())
    with col3:
        st.metric("Current Time", datetime.now().strftime("%H:%M"))

elif menu == "About":
    st.header("About This App")
    st.write("""
    This application demonstrates:
    - Streamlit functionality
    - Mobile-first development
    - Easy deployment
    - Interactive elements
    """)
    
    st.info("Built with ❤️ using Python and Streamlit")

# Footer
st.markdown("---")
st.markdown("Created on mobile 📱 • Powered by Streamlit ⚡")
