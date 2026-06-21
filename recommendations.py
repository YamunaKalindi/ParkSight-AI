import streamlit as st
import plotly.express as px
import pandas as pd


def show_recommendations(df):

    # ==================================================
    # HEADER
    # ==================================================

    st.title(
        "🚔 AI-Driven Enforcement Recommendations"
    )

    st.markdown(
        """
        Translate parking intelligence into actionable
        traffic management strategies by identifying
        priority zones and recommending targeted
        enforcement interventions.
        """
    )

    st.markdown("---")

    # ==================================================
    # RISK SUMMARY
    # ==================================================

    risk_counts = (
        df["risk_level"]
        .value_counts()
    )

    low_count = risk_counts.get("Low", 0)
    medium_count = risk_counts.get("Medium", 0)
    high_count = risk_counts.get("High", 0)
    critical_count = risk_counts.get("Critical", 0)

    critical_df = (
        df[
            df["risk_level"] == "Critical"
        ]
    )

    priority_zones = (
        critical_df
        .groupby("police_station")
        .size()
        .reset_index(
            name="critical_incidents"
        )
        .sort_values(
            "critical_incidents",
            ascending=False
        )
        .head(5)
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Locations Evaluated",
            f"{df['police_station'].nunique()}"
        )

    with c2:
        st.metric(
            "High Risk Incidents",
            f"{high_count:,}"
        )

    with c3:
        st.metric(
            "Critical Incidents",
            f"{critical_count:,}"
        )

    with c4:
        st.metric(
            "Priority Zones",
            f"{len(priority_zones)}"
        )

    st.markdown("---")

    # ==================================================
    # RISK DISTRIBUTION
    # ==================================================

    left, right = st.columns([1.3, 1])

    with left:

        st.subheader(
            "📊 Risk Distribution"
        )

        risk_df = (
            risk_counts
            .reset_index()
        )

        risk_df.columns = [
            "Risk Level",
            "Count"
        ]

        fig = px.pie(
            risk_df,
            names="Risk Level",
            values="Count",
            hole=0.55,
            color="Risk Level",
            color_discrete_map={
                "Low": "#94A3B8",
                "Medium": "#2563EB",
                "High": "#F59E0B",
                "Critical": "#DC2626"
            }
        )

        fig.update_layout(
            height=450
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

    with right:

        st.subheader(
            "What does this mean?"
        )

        st.markdown(
            f"""
            **Low Risk:** {low_count:,}

            Routine monitoring sufficient.

            **Medium Risk:** {medium_count:,}

            Preventive patrol recommended.

            **High Risk:** {high_count:,}

            Targeted enforcement required.

            **Critical Risk:** {critical_count:,}

            Immediate intervention required.
            """
        )

        st.info(
            """
            Higher risk levels indicate incidents
            estimated to create greater parking-induced
            congestion and therefore require greater
            enforcement priority.
            """
        )

    st.markdown("---")

    # ==================================================
    # PRIORITY ENFORCEMENT ZONES
    # ==================================================

    st.subheader(
        "🚨 Priority Enforcement Zones"
    )

    if len(priority_zones) > 0:

        display_df = (
            priority_zones
            .rename(
                columns={
                    "police_station":
                        "Police Station",
                    "critical_incidents":
                        "Critical Incidents"
                }
            )
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

        st.info(
            """
            These jurisdictions exhibit the highest concentration
            of Critical-risk incidents and should receive priority
            deployment of towing units, traffic personnel and
            temporary parking restrictions.
            """
        )

    else:

        st.success(
            "No critical enforcement zones identified."
        )

    st.markdown("---")

    # ==================================================
    # ENFORCEMENT RESPONSE MATRIX
    # ==================================================

    st.subheader(
        "🚦 Enforcement Response Matrix"
    )

    matrix = pd.DataFrame({

        "Risk Level": [
            "Low",
            "Medium",
            "High",
            "Critical"
        ],

        "Priority": [
            "P4",
            "P3",
            "P2",
            "P1"
        ],

        "Recommended Response": [

            "Routine Monitoring",

            "Preventive Patrolling",

            "Targeted Enforcement Drives",

            "Immediate Intervention and Tow Deployment"
        ]
    })

    st.dataframe(
        matrix,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # ==================================================
    # AI SUMMARY
    # ==================================================

    top_zone = (
        priority_zones
        .iloc[0]["police_station"]
        if len(priority_zones) > 0
        else "N/A"
    )

    st.subheader(
        "🤖 AI Recommendations"
    )

    st.markdown(
        f"""
### Key Insights

• Bengaluru exhibits clear spatial concentration
patterns in High and Critical risk incidents.

• **{top_zone}**
emerges as the highest priority enforcement zone.

• Resource allocation should prioritise towing units,
additional personnel and temporary parking restrictions
within identified hotspots.

• Continuous monitoring of these locations can
significantly reduce parking-induced congestion and
improve traffic flow efficiency.

• The system enables proactive deployment of
enforcement resources instead of reactive traffic
management.
        """
    )

    st.markdown("---")

    # ==================================================
    # DETAILS
    # ==================================================

    with st.expander(
            "📄 View Detailed Risk Data"
    ):

        detailed = (
            df
            .groupby(
                [
                    "police_station",
                    "risk_level"
                ]
            )
            .size()
            .reset_index(
                name="incident_count"
            )
            .sort_values(
                "incident_count",
                ascending=False
            )
        )

        st.dataframe(
            detailed,
            use_container_width=True
        )