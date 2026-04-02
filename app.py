import streamlit as st
import pandas as pd

st.set_page_config(page_title="Project 37", layout="wide")
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🚀 Project 37</h1>
    <h4 style='text-align: center;'>AI-Powered Early Risk Detection</h4>
    """,
    unsafe_allow_html=True
)
st.markdown("### 📝 Enter Patient Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age")
    gestation = st.number_input("Gestation Week")
    bp = st.number_input("Blood Pressure")

with col2:
    temp = st.number_input("Temperature (°C)")
    hb = st.number_input("Hemoglobin")
    wbc = st.number_input("WBC Count")

st.markdown("### 🤒 Symptoms")
fever = st.checkbox("Fever")
pain = st.checkbox("Abdominal Pain")
bleeding = st.checkbox("Bleeding")
fatigue = st.checkbox("Fatigue")

if st.button("🔍 Analyze Risk"):

    risk = 0
    drivers = []

    if temp > 37.5 and wbc > 11000:
        risk += 0.4
        drivers.append("Infection")

    if hb < 10:
        risk += 0.3
        drivers.append("Low Hemoglobin")

    if bp > 135:
        risk += 0.2
        drivers.append("High Blood Pressure")

    st.markdown("## 📊 Results")

    if risk > 0.6:
        st.error("🔴 High Risk")
        action = "Immediate monitoring required"
    elif risk > 0.3:
        st.warning("🟡 Medium Risk")
        action = "Regular monitoring advised"
    else:
        st.success("🟢 Low Risk")
        action = "Routine checkups sufficient"

    trend = "⬆ Increasing" if risk > 0.5 else "➡ Stable"

    st.write(f"**Risk Score:** {round(risk,2)}")
    st.write(f"**Trend:** {trend}")
    st.write(f"**Key Drivers:** {', '.join(drivers) if drivers else 'None'}")
    st.write(f"**Suggested Action:** {action}")

    st.markdown("### 📈 Risk Trend Over Time")

    data = pd.DataFrame({
        "Time": ["Visit 1", "Visit 2", "Visit 3", "Current"],
        "Risk Score": [max(risk-0.3,0), max(risk-0.2,0), max(risk-0.1,0), risk]
    })

    st.line_chart(data.set_index("Time"))

    st.markdown("---")
    st.markdown("### 🧾 Clinical Summary")

    st.info(f"""
    Risk Level: { "High" if risk>0.6 else "Medium" if risk>0.3 else "Low" }

    Primary Drivers: {', '.join(drivers) if drivers else 'None'}

    Recommended Action: {action}
    """)
