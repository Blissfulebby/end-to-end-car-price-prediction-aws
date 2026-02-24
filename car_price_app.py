import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('car_price.pkl')

# Page config
st.set_page_config(page_title='Car Price Predictor', layout='wide')

# --- Custom CSS for colors ---
st.markdown("""
<style>
/* Background of the whole page */
[data-testid="stAppViewContainer"] {
    background-color: #f0f8ff;
}

/* Section headers */
h1, h2, h3, h4 {
    color: #1f4e79;
}

/* Prediction box */
.prediction-box {
    background-color: #e6f2ff;
    border-radius: 10px;
    padding: 20px;
    margin: 20px 0;
    text-align: center;
}

/* Predicted price */
.predicted-price {
    color: #2e8b57;
    font-size: 3em;
}

/* Input labels */
.css-1fv8s86 {
    color: #333333;
}

/* Buttons */
.stButton>button {
    background-color: #1f78b4;
    color: white;
    border-radius: 8px;
}
.stButton>button:hover {
    background-color: #145a86;
}
</style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown("<h1 style='text-align: center;'>Car Price Prediction APP</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #333333;'>Fill in the car details below</p>", unsafe_allow_html=True)

# --- Input Fields ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h3>Vehicle Information</h3>", unsafe_allow_html=True)
    vehicle_age = st.slider('Vehicle Age (years)', 0, 30, 5, help="Age of the vehicle in years")
    km_driven = st.number_input('Kilometers Driven', 0, 1000000, 50000, step=1000, help="Total kilometers driven")

with col2:
    st.markdown("<h3>Performance Specifications</h3>", unsafe_allow_html=True)
    mileage = st.number_input('Mileage (kmpl)', 5.0, 50.0, 15.0, step=0.1, help="Fuel efficiency in kilometers per liter")
    max_power = st.number_input('Maximum Power (bhp)', 50.0, 1000.0, 100.0, step=1.0, help="Maximum power output in brake horsepower")

st.markdown("---")

# --- Prediction Button ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    if st.button('🚗 Predict Car Price', type='primary', use_container_width=True):
        try:
            input_data = pd.DataFrame({
                'vehicle_age': [vehicle_age],
                'km_driven': [km_driven],
                'mileage': [mileage],
                'max_power': [max_power]
            })
            prediction = model.predict(input_data)
            predicted_price = prediction[0]

            # Prediction Box
            st.markdown(f"""
            <div class='prediction-box'>
                <h2>Predicted Car Price</h2>
                <div class='predicted-price'>₦{predicted_price:,.0f}</div>
            </div>
            """, unsafe_allow_html=True)

            # Input summary
            st.subheader("📋 Input Summary")
            summary_col1, summary_col2 = st.columns(2)
            with summary_col1:
                st.metric("Vehicle Age", f"{vehicle_age} years")
                st.metric("Kilometers Driven", f"{km_driven:,} km")
            with summary_col2:
                st.metric("Mileage", f"{mileage} kmpl")
                st.metric("Max Power", f"{max_power} bhp")

            st.info('💡 This prediction is based on vehicle age, usage, fuel efficiency, and engine power.')

        except Exception as e:
            st.error(f'❌ Error making prediction: {str(e)}')
            st.info('Please make sure all fields are filled correctly and the model file is available.')

# --- About Section ---
st.markdown("---")
st.subheader("📊 About This Prediction Model")

with st.expander("🔍 How the prediction works"):
    st.write("""
    This car price prediction model uses a **Random Forest Regressor** trained on historical car sales data. 
    The model considers four key factors:
    
    - **Vehicle Age**: Older cars typically have lower values due to depreciation
    - **Kilometers Driven**: Higher mileage usually indicates more wear and tear
    - **Mileage (Fuel Efficiency)**: Better fuel economy can increase a car's value
    - **Maximum Power**: Higher engine power often correlates with higher car prices
    """)

with st.expander("📈 Model Performance"):
    st.write("""
    The Random Forest algorithm was chosen for its ability to:
    - Handle non-linear relationships between features
    - Provide robust predictions with multiple decision trees
    - Reduce overfitting through ensemble learning
    """)

with st.expander("⚠️ Important Notes"):
    st.write("""
    - Predictions are estimates based on historical data and may not reflect current market conditions
    - Actual car prices can vary based on additional factors like brand, model, condition, and location
    - This tool is for informational purposes only
    """)

# --- Footer ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.8em;'>Built with Streamlit 🚀 | Car Price Prediction Model</div>",
    unsafe_allow_html=True
)
