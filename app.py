
import streamlit as st
import pandas as pd

# -----------------------------
# CoastCrop AI
# -----------------------------

st.set_page_config(
    page_title="CoastCrop AI",
    page_icon="🌱",
    layout="centered"
)

# Load data
seasonal_data = pd.read_csv("coastcrop_seasonal_data.csv")
risk_data = pd.read_csv("coastcrop_climate_risk.csv")

# Planting calendar
crop_months = {
    "Watermelon": [1, 5, 9],
    "Sunflower": [11, 12],
    "Mung Bean": [2, 3, 8, 9],
    "Rice - BRRI dhan73": [8],
    "Tomato": [10, 11, 12]
}

month_names = {
    1: "January", 2: "February", 3: "March",
    4: "April", 5: "May", 6: "June",
    7: "July", 8: "August", 9: "September",
    10: "October", 11: "November", 12: "December"
}

# -----------------------------
# Header
# -----------------------------

st.title("🌱 CoastCrop AI")
st.subheader("Climate-Smart Farming for Coastal Bangladesh")

st.write(
    "CoastCrop AI combines climate and salinity information "
    "to provide simple crop-planning decision support."
)

st.divider()

# -----------------------------
# Farmer Inputs
# -----------------------------

st.header("🌾 Analyze Your Farm")

location = st.selectbox(
    "📍 Location",
    ["Khulna"]
)

month = st.selectbox(
    "📅 Expected Planting Month",
    list(range(1, 13)),
    format_func=lambda x: month_names[x],
    index=10
)

analyze = st.button(
    "🔍 ANALYZE MY FARM",
    use_container_width=True
)

# -----------------------------
# Analysis
# -----------------------------

if analyze:

    month_data = risk_data[
        risk_data["MONTH"] == month
    ]

    if month_data.empty:

        st.error("No climate data available for this month.")

    else:

        row = month_data.iloc[0]

        salinity = round(float(row["nsal"]), 2)
        climate_risk = round(float(row["climate_risk_score"]), 1)
        risk_level = str(row["risk_level"])

        compatible = [
            crop
            for crop, months in crop_months.items()
            if month in months
        ]

        st.success("Analysis completed!")

        # Climate information
        st.header("🌦️ Climate Conditions")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Salinity Index",
            salinity
        )

        col2.metric(
            "Climate Risk",
            climate_risk
        )

        col3.metric(
            "Risk Level",
            risk_level
        )

        # Recommendations
        st.header("🌾 Planting-Compatible Crops")

        if compatible:

            for i, crop in enumerate(compatible, 1):

                st.write(
                    f"**{i}. {crop}**"
                )

            st.info(
                "These crops match the current prototype "
                "planting-calendar and climate conditions."
            )

        else:

            st.warning(
                "No crop with a verified planting window "
                "was found for this month."
            )

        # Explanation
        st.header("💡 Why this recommendation?")

        st.write(
            f"For **{location}** in **{month_names[month]}**, "
            f"the available salinity index is **{salinity}** "
            f"and the prototype climate-risk score is "
            f"**{climate_risk}/100**."
        )

        # Safety
        st.warning(
            "Prototype decision-support system only. "
            "Recommendations are based on available data "
            "and require further agricultural validation."
        )

st.divider()

st.caption(
    "CoastCrop AI | Climate-smart agriculture prototype "
    "for coastal Bangladesh"
)
