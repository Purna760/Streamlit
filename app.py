import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px

# App configuration
st.set_page_config(
    page_title="My Mobile App",
    page_icon="📱",
    layout="centered"
)

# Custom CSS for mobile optimization
st.markdown("""
<style>
    /* Mobile-responsive adjustments */
    @media (max-width: 768px) {
        .main > div {
            padding: 1rem;
        }
        .stButton > button {
            width: 100%;
        }
        .stSelectbox, .stTextInput, .stSlider {
            width: 100%;
        }
    }
    
    .main {
        background-color: #f0f2f6;
    }
    
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.5rem;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #45a049;
        color: white;
    }
    
    .success-message {
        padding: 1rem;
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.5rem;
        color: #155724;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Title and description
st.title("📱 My Streamlit Mobile App")
st.markdown("**This app was created and deployed entirely from a mobile phone!** ✨")

# Sidebar
st.sidebar.header("📱 Navigation")
menu = st.sidebar.selectbox("Choose a section", 
    ["🏠 Home", "📊 Data Analysis", "🎯 Interactive Features", "ℹ️ About"])

# Sidebar feedback section
st.sidebar.markdown("---")
st.sidebar.subheader("💬 Feedback")
feedback = st.sidebar.text_area("How can we improve this app?")
if st.sidebar.button("Submit Feedback"):
    if feedback:
        st.sidebar.success("Thanks for your feedback! 💝")
        # In a real app, you'd save this to a database
    else:
        st.sidebar.warning("Please enter your feedback")

# Home Section
if menu == "🏠 Home":
    st.header("Welcome! 👋")
    
    # User input with session state
    st.subheader("👤 Personalize Your Experience")
    name = st.text_input("What's your name?", value=st.session_state.user_name)
    if name:
        st.session_state.user_name = name
        st.success(f"Hello, {name}! 👋 Welcome to your mobile-built app!")
    
    # Interactive elements
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎛️ Controls")
        age = st.slider("Select your age", 0, 100, 25)
        st.write(f"**Age:** {age} years")
        
        # Counter with session state
        if st.button("🎯 Click me!"):
            st.session_state.clicks += 1
            st.balloons()
        
        st.write(f"**Button clicks:** {st.session_state.clicks}")
    
    with col2:
        st.subheader("📈 Real-time Metrics")
        col2_1, col2_2, col2_3, col2_4 = st.columns(4)
        
        with col2_1:
            st.metric("Temperature", "24°C", "1.2°C")
        with col2_2:
            st.metric("Humidity", "65%", "-3%")
        with col2_3:
            st.metric("Users Online", "142", "8")
        with col2_4:
            st.metric("Performance", "98%", "2%")
    
    # Progress bar example
    st.subheader("⏳ Progress Demo")
    if st.button('Show Progress Bar'):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(f"Progress: {i + 1}%")
            # Simulate some processing time
            np.random.rand(1000, 1000)
        
        status_text.text("✅ Completed!")
        st.success("Progress finished successfully!")

# Data Analysis Section
elif menu == "📊 Data Analysis":
    st.header("Data Analysis 📊")
    
    # Generate sample data
    np.random.seed(42)
    data = pd.DataFrame({
        'x': np.random.randn(100),
        'y': np.random.randn(100),
        'category': np.random.choice(['A', 'B', 'C'], 100),
        'value': np.random.randint(1, 100, 100)
    })
    
    # Display data
    st.subheader("📋 Sample Data")
    st.dataframe(data.head(10))
    
    # Data summary
    st.subheader("📊 Data Summary")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Records", len(data))
    with col2:
        st.metric("Unique Categories", data['category'].nunique())
    with col3:
        st.metric("Average Value", f"{data['value'].mean():.1f}")
    
    # Charts
    st.subheader("📈 Visualizations")
    
    # Streamlit native chart
    st.write("**Streamlit Scatter Chart**")
    st.scatter_chart(data, x='x', y='y', color='category')
    
    # Plotly interactive chart
    st.write("**Interactive Plotly Chart**")
    fig = px.scatter(data, x='x', y='y', color='category', 
                     size='value', hover_data=['value'],
                     title="Interactive Scatter Plot with Plotly")
    st.plotly_chart(fig)
    
    # Data filtering
    st.subheader("🔍 Data Filtering")
    selected_category = st.selectbox("Select Category to Filter", 
                                   options=['All'] + list(data['category'].unique()))
    
    if selected_category == 'All':
        filtered_data = data
    else:
        filtered_data = data[data['category'] == selected_category]
    
    st.write(f"Showing {len(filtered_data)} records for category: {selected_category}")
    st.dataframe(filtered_data)
    
    # Download button
    st.subheader("💾 Export Data")
    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')

    csv = convert_df(data)
    st.download_button(
        "📥 Download Sample Data as CSV",
        csv,
        "mobile_app_data.csv",
        "text/csv",
        key='download-csv'
    )

# Interactive Features Section
elif menu == "🎯 Interactive Features":
    st.header("🎮 Interactive Features")
    
    # File uploader
    st.subheader("📁 File Upload Demo")
    uploaded_file = st.file_uploader("Choose a CSV or text file", 
                                   type=['csv', 'txt', 'xlsx'])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            
            st.success("✅ File uploaded successfully!")
            st.write(f"**File:** {uploaded_file.name}")
            st.write(f"**Shape:** {df.shape[0]} rows × {df.shape[1]} columns")
            st.dataframe(df.head())
        except Exception as e:
            st.error(f"Error reading file: {e}")
    
    # Color picker
    st.subheader("🎨 Color Picker")
    color = st.color_picker('Pick a color', '#00f900')
    st.write(f'Selected color: `{color}`')
    st.markdown(f'<div style="width:100%; height:50px; background-color:{color}; border-radius:10px;"></div>', 
                unsafe_allow_html=True)
    
    # Date input
    st.subheader("📅 Date Selector")
    selected_date = st.date_input("Select a date", datetime.now())
    st.write(f"Selected date: {selected_date}")
    
    # Multiple choice
    st.subheader("🔘 Multiple Choice")
    options = st.multiselect(
        'What are your favorite programming languages?',
        ['Python', 'JavaScript', 'Java', 'C++', 'Go', 'Rust'],
        ['Python'])
    st.write(f'You selected: {", ".join(options)}')
    
    # Session state counter
    st.subheader("🔢 Session State Counter")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("➕ Increment"):
            st.session_state.counter += 1
    with col2:
        if st.button("➖ Decrement"):
            st.session_state.counter -= 1
    with col3:
        if st.button("🔄 Reset"):
            st.session_state.counter = 0
    
    st.write(f"**Current count:** {st.session_state.counter}")

# About Section
elif menu == "ℹ️ About":
    st.header("ℹ️ About This App")
    
    st.markdown("""
    ## 🚀 Mobile-First Streamlit App
    
    This application demonstrates what's possible when building web applications 
    **entirely from a mobile device**!
    
    ### ✨ Features Included:
    
    - 📊 **Data Visualization** with interactive charts
    - 📱 **Mobile-optimized** responsive design
    - 🎮 **Interactive elements** (buttons, sliders, forms)
    - 💾 **File upload** and data processing
    - 📈 **Real-time metrics** and progress tracking
    - 💬 **User feedback** system
    - 🎨 **Custom styling** and themes
    
    ### 🛠️ Built With:
    
    - **Python** 🐍
    - **Streamlit** ⚡
    - **Pandas** 📊
    - **Plotly** 📈
    - **NumPy** 🔢
    
    ### 📲 Deployment:
    
    - Created on **Android mobile phone**
    - Deployed to **Streamlit Community Cloud**
    - Version controlled with **Git** from mobile
    - **No laptop or PC** used in development
    
    ### 🎯 What This Proves:
    
    You don't need expensive equipment to build and deploy web applications! 
    With just a mobile phone and free tools, you can create professional web apps.
    """)
    
    # Tech stack icons
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.markdown("**Python**")
        st.write("🐍")
    with col2:
        st.markdown("**Streamlit**")
        st.write("⚡")
    with col3:
        st.markdown("**Pandas**")
        st.write("📊")
    with col4:
        st.markdown("**Plotly**")
        st.write("📈")
    with col5:
        st.markdown("**Git**")
        st.write("📚")
    
    st.info("""
    💡 **Pro Tip**: This entire app was built using:
    - **Termux** (terminal emulator)
    - **QuickEdit** (text editor)
    - **GitHub Mobile** (version control)
    All free apps available on the Play Store!
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
        <p>📱 <strong>Created entirely on mobile</strong> • ⚡ <strong>Powered by Streamlit</strong></p>
        <p>🕒 Last updated: {} • 🔄 Auto-deploys on git push</p>
    </div>
    """.format(datetime.now().strftime("%Y-%m-%d %H:%M")),
    unsafe_allow_html=True
)

# Secret developer section (hidden feature)
with st.sidebar:
    if st.button("🐍 Developer Mode", key="dev_mode"):
        st.code("""
        # Mobile development commands:
        git add .
        git commit -m "Mobile update"
        git push origin main
        """)
