import streamlit as st
import pandas as pd
import plotly.express as px
from sklearn.ensemble import RandomForestClassifier

# Training data for AI Risk Prediction

X = [
    [90, 10],
    [80, 20],
    [70, 30],
    [60, 40],
    [50, 50],
    [40, 60],
    [30, 70],
    [20, 80]
]

# 0 = Low Risk
# 1 = High Risk

y = [0, 0, 0, 0, 1, 1, 1, 1]


# Create AI Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)


# Page Configuration
st.set_page_config(
    page_title="Tech Voyager",
    page_icon="🚀",
    layout="wide"
)


# Sidebar
st.sidebar.title("🚀 Tech Voyager")
st.sidebar.write("AI Project Management System")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "📁 Projects",
        "⚠️ Risk Analysis",
        "🤖 AI Predictions",
        "🔔 Alerts",
        "📄 Reports"
    ]
)


# ---------------- DASHBOARD ----------------

if page == "📊 Dashboard":

    st.title("📊 Tech Voyager Dashboard")
    st.write("Welcome to the AI Project Management System 🚀")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📁 Total Projects", "5")

    with col2:
        st.metric("⚠️ High Risk Projects", "2")

    with col3:
        st.metric("🤖 AI Predictions", "5")

    with col4:
        st.metric("🔔 Active Alerts", "3")

    st.divider()

    st.subheader("📊 Project Overview")

    dashboard_data = pd.DataFrame({
        "Project": [
            "AI Healthcare",
            "Smart Traffic",
            "E-Learning",
            "Bank Fraud",
            "Weather Prediction"
        ],
        "Progress": [80, 65, 90, 45, 70]
    })

    fig = px.bar(
        dashboard_data,
        x="Project",
        y="Progress",
        title="Overall Project Progress",
        text="Progress"
    )

    st.plotly_chart(fig, width="stretch")


# ---------------- PROJECTS ----------------

elif page == "📁 Projects":

    st.title("📁 Projects")
    st.write("Manage and monitor all your projects.")

    projects_data = {
        "Project": [
            "AI Healthcare System",
            "Smart Traffic Management",
            "E-Learning Platform",
            "Bank Fraud Detection",
            "Weather Prediction System"
        ],
        "Progress": [80, 65, 90, 45, 70],
        "Status": [
            "On Track",
            "In Progress",
            "Completed",
            "Delayed",
            "In Progress"
        ]
    }

    projects = pd.DataFrame(projects_data)

    st.subheader("📊 Interactive Project Progress")

    fig = px.bar(
        projects,
        x="Project",
        y="Progress",
        color="Status",
        title="Project Progress Overview",
        text="Progress"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("📋 Project Details")

    st.dataframe(projects, width="stretch")


# ---------------- RISK ANALYSIS ----------------

elif page == "⚠️ Risk Analysis":

    st.title("⚠️ Risk Analysis")
    st.write("AI-based project risk monitoring and analysis.")

    risk_data = {
        "Project": [
            "AI Healthcare System",
            "Smart Traffic Management",
            "E-Learning Platform",
            "Bank Fraud Detection",
            "Weather Prediction System"
        ],
        "Risk Level": [
            "Medium",
            "High",
            "Low",
            "High",
            "Medium"
        ],
        "Risk Score": [55, 85, 20, 90, 60]
    }

    risks = pd.DataFrame(risk_data)

    st.subheader("📊 Interactive Risk Analysis")

    fig = px.bar(
        risks,
        x="Project",
        y="Risk Score",
        color="Risk Level",
        title="Project Risk Scores",
        text="Risk Score"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("📋 Risk Details")

    st.dataframe(risks, width="stretch")

    st.warning(
        "⚠️ High-risk projects require immediate attention!"
    )


# ---------------- AI PREDICTIONS ----------------

elif page == "🤖 AI Predictions":

    st.title("🤖 AI Predictions")

    st.write("Machine Learning based project risk prediction.")

    st.divider()

    st.subheader("🔮 Predict Project Risk")

    progress = st.slider(
        "Project Progress (%)",
        min_value=0,
        max_value=100,
        value=50
    )

    risk = st.slider(
        "Risk Percentage (%)",
        min_value=0,
        max_value=100,
        value=50
    )

    if st.button("🤖 Predict Risk"):

        prediction = model.predict([[progress, risk]])

        if prediction[0] == 1:

            st.error("🔴 HIGH RISK PROJECT!")

            st.write(
                "⚠️ The AI model predicts that this project may require immediate attention."
            )

        else:

            st.success("🟢 LOW RISK PROJECT!")

            st.write(
                "✅ The AI model predicts that this project is performing well."
            )
# ---------------- ALERTS ----------------

elif page == "🔔 Alerts":

    st.title("🔔 Project Alerts")
    st.write("Important notifications and early-warning alerts.")

    st.error(
        "🔴 HIGH RISK: Bank Fraud Detection project has a high probability of delay!"
    )

    st.warning(
        "🟡 WARNING: Smart Traffic Management project requires close monitoring."
    )

    st.info(
        "🔵 INFO: AI Healthcare System is progressing according to schedule."
    )

    st.success(
        "🟢 SUCCESS: E-Learning Platform is performing well and is on track."
    )

    st.success(
        "🟢 SUCCESS: Weather Prediction System is progressing normally."
    )

    st.divider()

    st.subheader("🚨 Alert Summary")

    alert_data = {
        "Alert Type": [
            "High Risk",
            "Medium Risk",
            "Normal"
        ],
        "Number of Projects": [
            1,
            1,
            3
        ]
    }

    alerts = pd.DataFrame(alert_data)

    fig = px.bar(
        alerts,
        x="Alert Type",
        y="Number of Projects",
        title="Project Alert Summary",
        text="Number of Projects"
    )

    st.plotly_chart(fig, width="stretch")


# ---------------- REPORTS ----------------

elif page == "📄 Reports":

    st.title("📄 Project Reports")
    st.write("Overall summary and performance analysis of all projects.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("📁 Total Projects", "5")

    with col2:
        st.metric("✅ Completed", "1")

    with col3:
        st.metric("⚠️ At Risk", "2")

    st.divider()

    report_data = {
        "Category": [
            "Completed",
            "In Progress",
            "Delayed"
        ],
        "Number of Projects": [
            1,
            3,
            1
        ]
    }

    reports = pd.DataFrame(report_data)

    st.subheader("📊 Overall Project Performance")

    fig = px.bar(
        reports,
        x="Category",
        y="Number of Projects",
        title="Project Performance Report",
        text="Number of Projects"
    )

    st.plotly_chart(fig, width="stretch")

    st.subheader("📋 Report Details")

    st.dataframe(reports, width="stretch")

    st.success(
        "✅ Project performance report generated successfully!"
    )

    csv = reports.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Report as CSV",
        data=csv,
        file_name="tech_voyager_report.csv",
        mime="text/csv"
    )