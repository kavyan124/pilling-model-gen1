import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Skincare Gen 1 Pilling Model",
    page_icon="🧴",
    layout="wide"
)

# Title and description
st.title("🧴 Skincare Gen 1 Pilling Model")
st.markdown("""
This tool predicts product pilling based on physical properties. Enter the measurements below 
to calculate the pilling score. **Higher values indicate more pilling.**
""")

# Create two columns for better layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Product Information")
    product_name = st.text_input("Product Name", value="Sample Product", help="Enter the product name for identification")
    
    st.subheader("Physical Properties")
    modulus = st.number_input(
        "Modulus",
        value=1.42,
        format="%.4f",
        help="Modulus measurement"
    )
    
    modulus_slope = st.number_input(
        "Modulus Slope",
        value=0.0365,
        format="%.4f",
        help="Slope of modulus curve"
    )
    
    avg_time_weighted_force_area = st.number_input(
        "Avg Time Weighted Force Area",
        value=0.0,
        format="%.2f",
        help="Average time-weighted force area"
    )
    
    area_prior_to_transition = st.number_input(
        "Area Prior to Transition",
        value=0.0,
        format="%.2f",
        help="Area measurement prior to transition"
    )
    
    avg_break_time_delta = st.number_input(
        "Avg Break Time Delta",
        value=0.58,
        format="%.4f",
        help="Average break time delta"
    )

with col2:
    st.subheader("Physical Properties (Continued)")
    max_break_time_delta = st.number_input(
        "Max Break Time Delta",
        value=0.0,
        format="%.4f",
        help="Maximum break time delta"
    )
    
    peak_100 = st.number_input(
        "Peak 100",
        value=0.0,
        format="%.2f",
        help="Peak 100 measurement"
    )
    
    plastic_viscosity = st.number_input(
        "Plastic Viscosity1 at 10s-1",
        value=0.0,
        format="%.2f",
        help="Plastic viscosity at 10s-1"
    )
    
    stress_ratio_curve = st.number_input(
        "Stress Ratio Curve 1:3 at 10s-1",
        value=0.0,
        format="%.4f",
        help="Stress ratio curve 1:3 at 10s-1"
    )

# Calculation button
st.divider()
if st.button("🔬 Calculate Pilling Score", type="primary", use_container_width=True):
    
    # Model 1 calculation
    model_1 = 100 * (
        0.000220315538715463
        + -0.0000001568439966864 * avg_time_weighted_force_area
        + 0.00570014992976465 * modulus
        + 0.0302313932460581 * (modulus - 1.42166666666667) ** 2
        + -5.6542741084434 * (modulus_slope - 0.0365000000000071) ** 2
    )
    
    # Model 2 calculation
    model_2 = 100 * (
        -0.00770489933407833
        + 0.00717684542217111 * avg_break_time_delta
        + 0.00308189097848233 * modulus
        + 0.0000371164264743504 * area_prior_to_transition
        + (avg_break_time_delta - 0.577939814814826) ** 2 * 0.0106100132525713
        + (modulus - 1.42166666666667) ** 2 * 0.0160081282677131
    )
    
    # Model 3 calculation
    model_3 = 100 * (
        -0.0110921259127157
        + 0.00455149055472188 * max_break_time_delta
        + -0.0000079791849131521 * peak_100
        + 0.0000051881224585033 * plastic_viscosity
        + 0.0143971810284143 * stress_ratio_curve
        + (modulus - 1.42166666666667) ** 2 * 0.0160557017221942
    )
    
    # Apply zero floor and calculate average (excluding negative values from average)
    averageUsesZeros = False  # Set to True to include zeros in average
    
    if averageUsesZeros:
        model_1_result = max(0, model_1)
        model_2_result = max(0, model_2)
        model_3_result = max(0, model_3)
        avg_denom = 3
    else:
        avg_denom = 3
        model_1_result = max(0, model_1)
        if model_1 < 0:
            avg_denom -= 1
        
        model_2_result = max(0, model_2)
        if model_2 < 0:
            avg_denom -= 1
        
        model_3_result = max(0, model_3)
        if model_3 < 0:
            avg_denom -= 1
    
    avg_result = (model_1_result + model_2_result + model_3_result) / avg_denom if avg_denom > 0 else 0
    
    # Display results
    st.divider()
    st.subheader(f"📊 Results for: {product_name}")
    
    # Create columns for results
    res_col1, res_col2, res_col3, res_col4 = st.columns(4)
    
    with res_col1:
        st.metric("Model 1", f"{model_1_result:.3f}")
    
    with res_col2:
        st.metric("Model 2", f"{model_2_result:.3f}")
    
    with res_col3:
        st.metric("Model 3", f"{model_3_result:.3f}")
    
    with res_col4:
        st.metric("Average Score", f"{avg_result:.3f}", 
                 help="Average of the three models (excluding negative predictions)")
    
    # Note about negative values
    st.info("ℹ️ **Note:** If any model predicts a negative value, it is set to zero before calculating the average.")
    
    # Interpretation
    st.divider()
    st.subheader("📝 Interpretation")
    
    if avg_result < 1.0:
        st.success("✅ **Low Pilling Risk** - This formulation has minimal predicted pilling.")
    elif avg_result < 3.0:
        st.warning("⚠️ **Moderate Pilling Risk** - Some pilling may occur with this formulation.")
    else:
        st.error("❌ **High Pilling Risk** - This formulation is predicted to have significant pilling.")
    
    # Show raw model values (before zero floor)
    with st.expander("🔍 View Raw Model Values (Before Zero Floor)"):
        st.write(f"**Model 1 Raw:** {model_1:.3f}")
        st.write(f"**Model 2 Raw:** {model_2:.3f}")
        st.write(f"**Model 3 Raw:** {model_3:.3f}")

# Footer
st.divider()
st.caption("💡 Tip: Higher pilling scores indicate greater likelihood of product pilling on the skin.")
