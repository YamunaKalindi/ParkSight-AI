import streamlit as st
import plotly.express as px
import pandas as pd
import re
import time


def show_overview(
        df,
        junction_df,
        station_df,
        hourly_df
):

    # =====================================================
    # HELPERS
    # =====================================================

    def clean_violation(x):
        x = str(x)

        x = x.replace("[", "")
        x = x.replace("]", "")
        x = x.replace("'", "")
        x = x.replace('"', "")

        x = x.replace(",", " & ")

        return x.title()

    peak_hour = (
        hourly_df
        .sort_values(
            "avg_cis",
            ascending=False
        )
        .iloc[0]["hour"]
    )

    high_risk = (
        df["risk_level"] == "High"
    ).sum()

    critical_risk = (
        df["risk_level"] == "Critical"
    ).sum()

    # =====================================================
    # HEADER
    # =====================================================

    st.title("🚦 ParkSight AI")

    st.markdown(
        """
        ### Intelligent Parking-Induced Congestion Monitoring and Enforcement System

        AI-driven parking intelligence platform for identifying illegal parking hotspots,
        estimating congestion impact and supporting data-driven traffic enforcement decisions.
        """
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # =====================================================
    # EXECUTIVE SUMMARY
    # =====================================================

    st.header("Executive Summary")

    total_violations = len(df)
    avg_cis = round(df["cis"].mean(), 2)
    stations = df["police_station"].nunique()
    junctions = df["junction_name"].nunique()

    # ---------------- Row 1 ----------------

    c1, c2 = st.columns(2)

    with c1:

        counter = st.empty()

        for i in range(0, total_violations + 1, 5000):
            counter.metric(
                "Total Violations",
                f"{i:,}"
            )
            time.sleep(0.03)

        counter.metric(
            "Total Violations",
            f"{total_violations:,}"
        )

    with c2:

        counter = st.empty()

        for i in range(0, int(avg_cis * 100) + 1, 200):
            counter.metric(
                "Average CIS - Congestion Impact Score",
                f"{i / 100:.2f}/100"
            )
            time.sleep(0.03)
        counter.metric(
            "Average CIS",
            f"{avg_cis:.2f}/100"
        )

    st.markdown("")

    # ---------------- Row 2 ----------------

    c3, c4 = st.columns(2)

    with c3:

        st.metric(
            "Analysis Period",
            "Nov 2023 - Apr 2024"
        )

    with c4:

        st.metric(
            "Coverage",
            f"{stations} Police Stations | "
            f"{junctions} Junctions"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    # =====================================================
    # KEY OBSERVATIONS
    # =====================================================

    st.header("Key Observations")

    left, right = st.columns([1.5, 1])

    with left:

        st.markdown(
            f"""
            #### What was observed?

            Bengaluru recorded **{len(df):,} illegal parking incidents**
            between **November 2023 and April 2024**.

            These incidents span across
            **{df['police_station'].nunique()} police stations**
            and
            **{df['junction_name'].nunique()} monitored junctions**.

            ParkSight AI estimates the congestion impact of every incident
            using the **Congestion Impact Score (CIS)** and identifies
            locations requiring priority enforcement.
            """
        )

    with right:

        st.info(
            f"""
            **Major Findings**

            • Peak congestion occurs around **{int(peak_hour)}:00 hrs**

            • **{high_risk:,} incidents**
            fall under High Risk category

            • **{critical_risk:,} incidents**
            require immediate intervention
            """
        )

    st.markdown("---")

    # =====================================================
    # VISUAL ANALYTICS
    # =====================================================

    c1, c2 = st.columns(2)

    # =====================================================
    # TOP VIOLATIONS
    # =====================================================

    with c1:

        st.subheader("Top Violation Types")

        violation_counts = (
            df["violation_type"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        violation_counts.columns = [
            "Violation",
            "Count"
        ]

        violation_counts["Violation"] = (
            violation_counts["Violation"]
            .apply(clean_violation)
        )

        fig = px.bar(
            violation_counts,
            x="Count",
            y="Violation",
            orientation="h",
            color="Count",
            color_continuous_scale="Blues",
            title="Most Frequent Parking Violations"
        )

        fig.update_layout(
            height=500,
            coloraxis_showscale=False,
            yaxis=dict(
                categoryorder="total ascending"
            ),
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.caption(
            """
            This chart shows the most frequently occurring parking violations.
            Wrong Parking and No Parking violations dominate the dataset,
            indicating recurring enforcement challenges in high-density corridors.
            """
        )

    # =====================================================
    # VEHICLE DISTRIBUTION
    # =====================================================

    with c2:

        st.subheader("Vehicle Distribution")

        vehicle_counts = (
            df["vehicle_type"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        vehicle_counts.columns = [
            "Vehicle",
            "Count"
        ]

        fig = px.pie(
            vehicle_counts,
            names="Vehicle",
            values="Count",
            hole=0.45,
            title="Vehicle Types Involved in Violations",
            color_discrete_sequence=[
                "#1E3A8A",
                "#2563EB",
                "#3B82F6",
                "#60A5FA",
                "#0F766E",
                "#14B8A6",
                "#F97316",
                "#EF4444",
                "#64748B",
                "#94A3B8"
            ]
        )

        fig.update_layout(
            height=500,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={
                "displayModeBar": False
            }
        )

        st.caption(
            """
            This chart illustrates the distribution of vehicle categories involved
            in illegal parking incidents. The dominance of private vehicles suggests
            that enforcement efforts should focus on locations experiencing high
            personal vehicle density.
            """
        )

    st.markdown("---")

    # =====================================================
    # CONGESTION TREND
    # =====================================================

    st.header("Congestion Impact Throughout the Day")

    fig = px.line(
        hourly_df,
        x="hour",
        y="avg_cis",
        markers=True,
        title="Average Congestion Impact by Hour"
    )

    fig.update_traces(
        line=dict(
            width=4
        ),
        marker=dict(
            size=8
        )
    )

    fig.update_layout(
        xaxis_title="Hour of Day",
        yaxis_title="Average CIS",
        height=450,
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )

    left, right = st.columns([2, 1])

    with left:

        st.markdown(
            f"""
            #### Interpretation

            Illegal parking incidents exhibit a clear temporal concentration pattern.

            Congestion gradually increases during the morning,
            reaches its highest level around **{int(peak_hour)}:00 hours**,
            and declines during the later parts of the day.

            These recurring patterns indicate that parking-induced congestion
            is predictable and therefore suitable for proactive enforcement planning.
            """
        )

    with right:

        st.info(
            f"""
            **Recommended Action**

            🚔 Increase patrol frequency
            between 09:00–13:00.

            🚛 Deploy towing resources
            during peak periods.

            🚦 Prioritise high-risk
            junction monitoring around
            **{int(peak_hour)}:00 hrs**.
            """
        )