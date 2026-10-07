# 🌱 CoastCrop AI

### Climate-Smart Farming for Coastal Bangladesh

CoastCrop AI is a prototype AI-powered decision-support system designed to help farmers in coastal Bangladesh make more informed crop-planning decisions under climate and salinity risks.

## 🌍 The Problem

Coastal farmers in Bangladesh face increasing uncertainty due to salinity intrusion, flooding, changing rainfall patterns, and limited freshwater availability.

These conditions can affect:

- What crops farmers should plant
- When they should plant
- How climate and salinity may affect crop decisions
- How farmers can respond to changing environmental conditions

CoastCrop AI aims to turn climate and agricultural information into simple, understandable decision support.

## 🤖 How CoastCrop AI Works

The prototype combines:

- Climate information
- Salinity information
- Crop planting-calendar information
- Machine-learning-based salinity prediction

The current prototype uses a **Random Forest Regression** model to estimate a salinity index from available environmental variables.

The system then provides:

- Predicted salinity index
- Historical salinity index
- Climate-risk score
- Risk level
- Planting-compatible crops
- A simple explanation of the recommendation

## 📊 Data Sources

The prototype uses:

- World Bank coastal Bangladesh salinity data
- NASA POWER climate data
- Agricultural planting-calendar information

The current MVP focuses on **Khulna** as the demonstration location.

## 🧠 AI Approach

A Random Forest Regression model is used for prototype salinity-index prediction.

Input variables include:

- Month
- Average temperature
- Average rainfall
- Salinity-related measurement

The model is intended as an initial prototype and has not yet been validated for operational agricultural decision-making.

## 🌾 Current MVP

Current prototype features:

- Location selection
- Planting-month selection
- AI-based salinity prediction
- Climate-risk assessment
- Crop planting compatibility
- Farmer-friendly explanation
- Safety and uncertainty notice

## ⚠️ Limitations

This is an early research prototype.

The available salinity dataset is small and the current MVP covers only one demonstration location. Crop suitability and planting-calendar information also require further field validation.

The model should therefore **not be treated as guaranteed agricultural advice**.

## 🔬 Future Validation Plan

Future validation will include:

1. Testing the model with additional coastal locations
2. Expanding climate and salinity datasets
3. Comparing predictions with observed field conditions
4. Working with agricultural experts
5. Conducting a small farmer usability study
6. Measuring whether users can understand and correctly apply the recommendations

## 🚀 Future Development

Future versions may include:

- More coastal districts and upazilas
- Flood-risk prediction
- Water-management recommendations
- More crop varieties
- Weather forecasting integration
- Bangla-language farmer interface
- Mobile-friendly access
- Local agricultural expert validation

## 🌱 Safety Statement

CoastCrop AI is a decision-support prototype, not a substitute for professional agricultural advice.

Recommendations are based on available data and prototype model predictions and should be validated with local agricultural experts before major farming decisions.

## 👩‍💻 Project

**CoastCrop AI: An AI-Powered Decision Support System for Climate-Smart Agriculture in Coastal Bangladesh**

Built as a prototype for the **AI4Climate Global Youth Climate Solutions Challenge 2026**.
