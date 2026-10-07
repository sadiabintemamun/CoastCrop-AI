import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

st.set_page_config(
    page_title="CoastCrop AI",
    page_icon="🌱",
    layout="centered"
)

# -----------------------------
# Load project data
# -----------------------------
seasonal_data = pd.read_csv("coastcrop_seasonal_data.csv")
risk_data = pd.read_csv("coastcrop_climate_risk.csv")

# -----------------------------
# Train prototype AI model
# -----------------------------
model_data = seasonal_data.copy()

X = model_data[["MONTH", "temperature_avg", "rainfall_avg", "msal"]]
y = model_data["nsal"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# Crop planting calendar
# -----------------------------
crop_months = {
    "Watermelon": [1, 5, 9],
    "Sunflower": [11, 12],
    "Mung Bean": [2, 3, 8, 9],
    "Rice - BRRI dhan73": [8],
    "Tomato": [10, 11, 12]
}

month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# -----------------------------
# App interface
# -----------------------------
st.title("🌱 CoastCrop AI")
st.subheader("Climate-Smart Farming for Coastal Bangladesh")

st.write(
    "CoastCrop AI combines climate, salinity and crop-calendar "
    "information to provide prototype decision support for coastal farmers."
)

st.divider()

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

    month_data = seasonal_data[
        seasonal_data["MONTH"] == month
    ]

    if month_data.empty:

        st.error("No climate data available for this month.")

    else:

        row = month_data.iloc[0]

        temperature = float(row["temperature_avg"])
        rainfall = float(row["rainfall_avg"])
        msal = float(row["msal"])
        actual_salinity = float(row["nsal"])

        # AI model prediction
        ai_prediction = model.predict(
            [[month, temperature, rainfall, msal]]
        )[0]

        ai_prediction = max(0, min(100, ai_prediction))

        climate_row = risk_data[
            risk_data["MONTH"] == month
        ]

        if not climate_row.empty:
            climate_risk = float(
                climate_row.iloc[0]["climate_risk_score"]
            )
            risk_level = str(
                climate_row.iloc[0]["risk_level"]
            )
        else:
            climate_risk = 0
            risk_level = "Unknown"

        compatible = [
            crop
            for crop, months in crop_months.items()
            if month in months
        ]

        st.success("Analysis completed!")

        st.header("🤖 AI Salinity Prediction")

        col1, col2 = st.columns(2)

        col1.metric(
            "Predicted Salinity Index",
            round(ai_prediction, 2)
        )

        col2.metric(
            "Historical Salinity Index",
            round(actual_salinity, 2)
        )

        st.header("🌦️ Climate Conditions")

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Temperature",
            f"{temperature:.1f} °C"
        )

        col2.metric(
            "Rainfall",
            f"{rainfall:.1f} mm"
        )

        col3.metric(
            "Climate Risk",
            f"{climate_risk:.1f}/100"
        )

        st.write(
            f"**Risk Level:** {risk_level}"
        )

        st.header("🌾 Planting-Compatible Crops")

        if compatible:

            for i, crop in enumerate(
                compatible,
                1
            ):
                st.write(
                    f"**{i}. {crop}**"
                )

            st.info(
                "These crops match the current prototype "
                "planting-calendar information for the selected month."
            )

        else:

            st.warning(
                "No crop with a verified prototype "
                "planting window was found for this month."
            )

        st.header("💡 Why this recommendation?")

        st.write(
            f"For **{location}** in **{month_names[month]}**, "
            f"the AI model estimates a salinity index of "
            f"**{ai_prediction:.2f}** using month, temperature, "
            f"rainfall and salinity-related input data."
        )

        st.caption(
            "The AI model is a prototype trained on a small "
            "coastal Bangladesh dataset and requires further "
            "validation before real-world agricultural use."
        )

        st.warning(
            "⚠️ Decision-support prototype only. "
            "Recommendations are not guaranteed agricultural advice."
        )

st.divider()

st.caption(
    "CoastCrop AI | Climate-smart agriculture prototype for coastal Bangladesh"
)
