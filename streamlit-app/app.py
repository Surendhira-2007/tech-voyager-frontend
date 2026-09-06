import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Tech Voyager",
    page_icon="🚀",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

div[data-testid="stMetric"] {
    background-color: #f7f9fc;
    border: 1px solid #e6e9ef;
    padding: 18px;
    border-radius: 12px;
}

.ai-box {
    background-color: #f7f9fc;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #e6e9ef;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PROJECT DATA
# =========================================================

projects_data = {

    "Project": [
        "AI Healthcare System",
        "Smart Traffic Management",
        "E-Learning Platform",
        "Bank Fraud Detection",
        "Weather Prediction System",
        "Smart Agriculture"
    ],

    "Progress": [
        80,
        65,
        90,
        45,
        70,
        55
    ],

    "Status": [
        "On Track",
        "In Progress",
        "Completed",
        "Delayed",
        "On Track",
        "In Progress"
    ],

    "Risk Score": [
        30,
        55,
        15,
        85,
        40,
        60
    ]
}


projects = pd.DataFrame(projects_data)


# =========================================================
# AI TRAINING DATA
# =========================================================

training_data = pd.DataFrame({

    "Project_Progress": [

        95, 92, 90, 88, 85,
        82, 80, 78, 75, 72,
        70, 68, 65, 62, 60,
        55, 50, 45, 40, 35,
        30, 25, 20, 15, 10

    ],

    "Project_Type": [

        "Software", "AI", "Web", "Software", "AI",
        "Web", "Software", "AI", "Web", "Software",
        "AI", "Web", "Software", "AI", "Web",
        "Software", "AI", "Web", "Software", "AI",
        "Web", "Software", "AI", "Web", "Software"

    ],

    "Risk_Percentage": [

        5, 8, 10, 12, 15,
        18, 20, 22, 25, 28,
        30, 35, 38, 42, 45,
        50, 55, 60, 65, 70,
        75, 80, 85, 90, 95

    ]

})


# =========================================================
# AI MODEL CLASS
# =========================================================

class PaimanaCoreAIModel:

    def __init__(self, data_source):

        self.df = data_source.copy()

        self.model = None

        self.metrics = {}

        self.feature_columns = None


    # =====================================================
    # CLEAN AND ENGINEER FEATURES
    # =====================================================

    def clean_and_engineer_features(
        self,
        target_column,
        numerical_cols,
        categorical_cols
    ):

        for col in numerical_cols:

            self.df[col] = pd.to_numeric(
                self.df[col],
                errors="coerce"
            )

            self.df[col] = self.df[col].fillna(
                self.df[col].median()
            )


        for col in categorical_cols:

            self.df[col] = (
                self.df[col]
                .fillna("UNKNOWN")
                .astype(str)
                .str.strip()
            )


        processed_df = pd.get_dummies(

            self.df[
                numerical_cols + categorical_cols
            ],

            columns=categorical_cols

        )


        X = processed_df

        y = self.df[target_column]


        return X, y


    # =====================================================
    # TRAIN AI MODEL
    # =====================================================

    def train_predictive_engine(

        self,
        target_column,
        numerical_cols,
        categorical_cols

    ):


        X, y = self.clean_and_engineer_features(

            target_column,

            numerical_cols,

            categorical_cols

        )


        self.feature_columns = X.columns


        X_train, X_test, y_train, y_test = (

            train_test_split(

                X,

                y,

                test_size=0.25,

                random_state=42

            )

        )


        # Random Forest AI Model

        self.model = RandomForestRegressor(

            n_estimators=100,

            random_state=42

        )


        # Train

        self.model.fit(

            X_train,

            y_train

        )


        # Predict test data

        predictions = self.model.predict(

            X_test

        )


        # AI Metrics

        self.metrics["MAE"] = (

            mean_absolute_error(

                y_test,

                predictions

            )

        )


        self.metrics["RMSE"] = (

            np.sqrt(

                mean_squared_error(

                    y_test,

                    predictions

                )

            )

        )


        self.metrics["R2 Score"] = (

            r2_score(

                y_test,

                predictions

            )

        )


        # Feature Importance

        feature_importance = pd.DataFrame({

            "Feature": X.columns,

            "Importance": self.model.feature_importances_

        })


        feature_importance = (

            feature_importance

            .sort_values(

                by="Importance",

                ascending=False

            )

        )


        return (

            X,

            self.metrics,

            feature_importance

        )


    # =====================================================
    # PREDICT RISK
    # =====================================================

    def predict_risk(

        self,

        progress,

        project_type

    ):


        input_data = pd.DataFrame({

            "Project_Progress": [

                progress

            ],

            "Project_Type": [

                project_type

            ]

        })


        input_encoded = pd.get_dummies(

            input_data

        )


        input_encoded = (

            input_encoded

            .reindex(

                columns=self.feature_columns,

                fill_value=0

            )

        )


        prediction = self.model.predict(

            input_encoded

        )[0]


        prediction = max(

            0,

            min(

                100,

                prediction

            )

        )


        return prediction


# =========================================================
# TRAIN AI MODEL
# =========================================================

ai_engine = PaimanaCoreAIModel(

    training_data

)


X, metrics, feature_importance = (

    ai_engine.train_predictive_engine(

        target_column="Risk_Percentage",

        numerical_cols=[

            "Project_Progress"

        ],

        categorical_cols=[

            "Project_Type"

        ]

    )

)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🚀 Tech Voyager")

st.sidebar.caption(
    "AI Powered Project Management"
)

st.sidebar.divider()


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


# =========================================================
# DASHBOARD
# =========================================================

if page == "📊 Dashboard":

    st.title("🚀 Tech Voyager Dashboard")

    st.write(
        "Welcome to your AI-powered project management portal."
    )


    st.divider()


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(

        "📁 Total Projects",

        len(projects)

    )


    high_risk = len(

        projects[
            projects["Risk Score"] >= 70
        ]

    )


    col2.metric(

        "⚠️ High Risk",

        high_risk

    )


    completed = len(

        projects[
            projects["Status"] == "Completed"
        ]

    )


    col3.metric(

        "✅ Completed",

        completed

    )


    average_progress = (

        projects["Progress"].mean()

    )


    col4.metric(

        "📈 Avg Progress",

        f"{average_progress:.1f}%"

    )


    st.divider()


    st.subheader(
        "📊 Interactive Project Progress"
    )


    fig = px.bar(

        projects,

        x="Project",

        y="Progress",

        color="Status",

        text="Progress",

        title="Project Progress Overview"

    )


    st.plotly_chart(

        fig,

        width="stretch"

    )


    st.subheader(
        "📋 Project Overview"
    )


    st.dataframe(

        projects,

        width="stretch"

    )


# =========================================================
# PROJECTS PAGE
# =========================================================

elif page == "📁 Projects":

    st.title("📁 Projects")

    st.write(
        "View and monitor all active projects."
    )


    st.divider()


    fig = px.bar(

        projects,

        x="Project",

        y="Progress",

        color="Status",

        text="Progress",

        title="Project Progress"

    )


    st.plotly_chart(

        fig,

        width="stretch"

    )


    st.dataframe(

        projects,

        width="stretch"

    )


# =========================================================
# RISK ANALYSIS
# =========================================================

elif page == "⚠️ Risk Analysis":

    st.title("⚠️ Risk Analysis")

    st.write(
        "Analyze possible risks across projects."
    )


    st.divider()


    projects["Risk Level"] = np.where(

        projects["Risk Score"] >= 70,

        "High Risk",

        np.where(

            projects["Risk Score"] >= 40,

            "Medium Risk",

            "Low Risk"

        )

    )


    fig = px.bar(

        projects,

        x="Project",

        y="Risk Score",

        color="Risk Level",

        text="Risk Score",

        title="Project Risk Analysis"

    )


    st.plotly_chart(

        fig,

        width="stretch"

    )


    st.dataframe(

        projects,

        width="stretch"

    )


# =========================================================
# AI PREDICTIONS PAGE
# =========================================================

elif page == "🤖 AI Predictions":

    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    st.title("🤖 AI Predictions")

    st.write(
        "Machine Learning powered project risk prediction and analysis."
    )


    st.divider()


    # -----------------------------------------------------
    # PREDICTION INPUT
    # -----------------------------------------------------

    st.subheader(
        "✨ Predict Project Risk"
    )


    input_col1, input_col2 = st.columns(2)


    with input_col1:

        project_progress = st.slider(

            "📊 Project Progress (%)",

            min_value=0,

            max_value=100,

            value=65

        )


    with input_col2:

        project_type = st.selectbox(

            "💻 Project Type",

            [

                "Software",

                "AI",

                "Web"

            ]

        )


    st.write("")


    predict_button = st.button(

        "🤖 Predict Risk",

        type="primary",

        use_container_width=True

    )


    st.divider()


    # -----------------------------------------------------
    # AI MODEL METRICS
    # -----------------------------------------------------

    st.subheader(
        "📊 AI Model Performance"
    )


    metric_col1, metric_col2, metric_col3 = (

        st.columns(3)

    )


    with metric_col1:

        st.metric(

            "🎯 MAE",

            f"{metrics['MAE']:.2f}",

            help="Mean Absolute Error"

        )


    with metric_col2:

        st.metric(

            "📈 RMSE",

            f"{metrics['RMSE']:.2f}",

            help="Root Mean Squared Error"

        )


    with metric_col3:

        r2_value = metrics["R2 Score"]


        st.metric(

            "🏆 R² Score",

            f"{r2_value:.2f}",

            help="Model accuracy score"

        )


    st.divider()


    # -----------------------------------------------------
    # GRAPH + PREDICTION RESULT
    # -----------------------------------------------------

    graph_col, result_col = st.columns(2)


    # =====================================================
    # FEATURE IMPORTANCE GRAPH
    # =====================================================

    with graph_col:


        st.subheader(
            "📈 Top Predictive Feature Weights"
        )


        feature_chart = px.bar(

            feature_importance,

            x="Importance",

            y="Feature",

            orientation="h",

            text="Importance",

            title="Feature Importance"

        )


        feature_chart.update_traces(

            texttemplate="%{text:.2f}",

            textposition="outside"

        )


        feature_chart.update_layout(

            height=400,

            yaxis={

                "categoryorder":

                "total ascending"

            }

        )


        st.plotly_chart(

            feature_chart,

            width="stretch"

        )


    # =====================================================
    # PREDICTION RESULT
    # =====================================================

    with result_col:


        st.subheader(
            "🔮 Prediction Result"
        )


        if predict_button:


            predicted_risk = (

                ai_engine.predict_risk(

                    project_progress,

                    project_type

                )

            )


            # ---------------------------------------------
            # HIGH RISK
            # ---------------------------------------------

            if predicted_risk >= 70:


                st.error(
                    "🔴 HIGH RISK PROJECT"
                )


                st.warning(
                    "Immediate attention is recommended."
                )


            # ---------------------------------------------
            # MEDIUM RISK
            # ---------------------------------------------

            elif predicted_risk >= 40:


                st.warning(
                    "🟡 MEDIUM RISK PROJECT"
                )


                st.info(
                    "Regular monitoring is recommended."
                )


            # ---------------------------------------------
            # LOW RISK
            # ---------------------------------------------

            else:


                st.success(
                    "🟢 LOW RISK PROJECT"
                )


                st.info(
                    "The project appears to be performing well."
                )


            st.write("")


            st.metric(

                "🎯 Predicted Risk Percentage",

                f"{predicted_risk:.1f}%"

            )


            st.progress(

                int(predicted_risk)

            )


            st.caption(

                "Prediction generated using Random Forest Machine Learning model."

            )


        else:


            st.info(
                "👆 Enter project details and click "
                "**Predict Risk** to generate an AI prediction."
            )


    # -----------------------------------------------------
    # TRAINING DATA
    # -----------------------------------------------------

    st.divider()


    st.subheader(
        "🔢 Sample Training Data"
    )


    st.write(
        "The following data is used to train the AI prediction model."
    )


    st.dataframe(

        training_data,

        width="stretch",

        hide_index=True

    )


    st.caption(

        f"Total Training Records: {len(training_data)}"

    )


# =========================================================
# ALERTS
# =========================================================

elif page == "🔔 Alerts":

    st.title("🔔 Early Warning Alerts")

    st.write(
        "AI-powered project monitoring alerts."
    )


    st.divider()


    for index, row in projects.iterrows():

        if row["Risk Score"] >= 70:


            st.error(

                f"🔴 HIGH RISK: "
                f"{row['Project']} "
                f"requires immediate attention."

            )


        elif row["Risk Score"] >= 40:


            st.warning(

                f"🟡 WARNING: "
                f"{row['Project']} "
                f"requires monitoring."

            )


        else:


            st.success(

                f"🟢 SAFE: "
                f"{row['Project']} "
                f"is performing well."

            )


# =========================================================
# REPORTS
# =========================================================

elif page == "📄 Reports":

    st.title("📄 Project Reports")

    st.write(
        "Project performance summary and downloadable reports."
    )


    st.divider()


    col1, col2, col3 = st.columns(3)


    col1.metric(

        "Total Projects",

        len(projects)

    )


    col2.metric(

        "Average Progress",

        f"{projects['Progress'].mean():.1f}%"

    )


    col3.metric(

        "Average Risk",

        f"{projects['Risk Score'].mean():.1f}%"

    )


    st.divider()


    st.subheader(
        "📋 Complete Project Report"
    )


    st.dataframe(

        projects,

        width="stretch"

    )


    csv = projects.to_csv(

        index=False

    )


    st.download_button(

        label="⬇️ Download CSV Report",

        data=csv,

        file_name="tech_voyager_report.csv",

        mime="text/csv",

        use_container_width=True

    )


# =========================================================
# SIDEBAR FOOTER
# =========================================================

st.sidebar.divider()

st.sidebar.caption(
    "🚀 Tech Voyager"
)

st.sidebar.caption(
    "AI Powered Executive Portal"
)