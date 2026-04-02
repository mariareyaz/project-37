if st.button("🔍 Analyze Risk"):

    risk = 0
    drivers = []

    # Age
    if age < 18 or age > 35:
        risk += 0.1
        drivers.append("Risky Maternal Age")

    # Temperature
    if temp > 38:
        risk += 0.2
        drivers.append("High Temperature")
    elif temp > 37.5:
        risk += 0.1

    # Blood Pressure
    if bp < 90:
        risk += 0.2
        drivers.append("Low Blood Pressure")
    elif bp < 100:
        risk += 0.1

    # WBC
    if wbc > 11000:
        risk += 0.2
        drivers.append("High WBC (Infection)")
    elif wbc > 10000:
        risk += 0.1

    # Hemoglobin
    if hb < 10:
        risk += 0.2
        drivers.append("Low Hemoglobin (Anemia)")
    elif hb < 11:
        risk += 0.1

    # Gestation
    if gestation < 34:
        risk += 0.2
        drivers.append("Early Gestation")
    elif gestation < 37:
        risk += 0.1

    # Symptoms
    if fever:
        risk += 0.1
        drivers.append("Fever")
    if pain:
        risk += 0.1
        drivers.append("Abdominal Pain")
    if bleeding:
        risk += 0.2
        drivers.append("Bleeding")
    if fatigue:
        risk += 0.05

    # RESULTS
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
