import streamlit as st
import plotly.express as px


def show_hotspots(
        junction_df,
        station_df,
        hourly_df
):

    # ==================================================
    # HEADER
    # ==================================================

    st.title(
        "🔥 Hotspots & Enforcement Prioritization"
    )

    st.markdown(
        """
        Identify the locations and time windows where illegal
        parking contributes most to congestion and prioritize
        traffic enforcement resources accordingly.
        """
    )

    st.markdown("---")

    # ==================================================
    # TOP N FILTER
    # ==================================================

    c1, c2 = st.columns([1, 4])

    with c1:

        top_n = st.selectbox(
            "Top Hotspots",
            [5, 10, 15, 20],
            index=0
        )

    st.markdown("---")

    # ==================================================
    # KPI CARDS
    # ==================================================

    top_junction = (
        junction_df
        .iloc[0]["junction_name"]
    )

    top_station = (
        station_df
        .iloc[0]["police_station"]
    )

    peak_hour = (
        hourly_df
        .sort_values(
            "avg_cis",
            ascending=False
        )
        .iloc[0]["hour"]
    )

    maximum_cis = (
        junction_df["max_cis"]
        .max()
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Most Critical Junction",
            top_junction
        )

    with c2:
        st.metric(
            "Most Critical Station",
            top_station
        )

    with c3:
        st.metric(
            "Peak Congestion Hour",
            f"{int(peak_hour):02d}:00"
        )

    with c4:
        st.metric(
            "Maximum CIS",
            f"{maximum_cis:.2f}"
        )

    st.markdown("---")

    # ==================================================
    # PREPARE DATA
    # ==================================================

    junction_top = (
        junction_df
        .head(top_n)
        .sort_values(
            "incidents"
        )
    )

    station_top = (
        station_df
        .head(top_n)
        .sort_values(
            "incidents"
        )
    )

    # ==================================================
    # SIDE BY SIDE CHARTS
    # ==================================================

    left, right = st.columns(2)

    # ==================================================
    # JUNCTION HOTSPOTS
    # ==================================================

    with left:

        st.subheader(
            f"📍 Top {top_n} Junction Hotspots"
        )

        fig = px.bar(
            junction_top,
            x="incidents",
            y="junction_name",
            orientation="h",
            text="incidents",
            color="incidents",
            color_continuous_scale="OrRd",
            labels={
                "incidents":
                    "Incidents",
                "junction_name":
                    "Junction"
            }
        )

        fig.update_layout(
            height=500,
            coloraxis_showscale=False,
            showlegend=False
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
            These junctions exhibit the highest concentration
            of illegal parking incidents and therefore require
            priority monitoring and enforcement interventions.
            """
        )

    # ==================================================
    # POLICE STATION HOTSPOTS
    # ==================================================

    with right:

        st.subheader(
            f"🚓 Top {top_n} Police Stations"
        )

        fig = px.bar(
            station_top,
            x="incidents",
            y="police_station",
            orientation="h",
            text="incidents",
            color="incidents",
            color_continuous_scale="Blues",
            labels={
                "incidents":
                    "Incidents",
                "police_station":
                    "Police Station"
            }
        )

        fig.update_layout(
            height=500,
            coloraxis_showscale=False,
            showlegend=False
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
            These police station jurisdictions experience
            the highest parking-induced congestion burden and
            should receive additional enforcement resources.
            """
        )

    st.markdown("---")

    # ==================================================
    # KEY FINDINGS
    # ==================================================

    st.subheader(
        "💡 Key Findings"
    )

    st.markdown(
        f"""
        - **{top_junction}** emerges as the most critical
        junction hotspot.

        - **{top_station}** experiences the highest
        congestion burden among police jurisdictions.

        - The highest congestion impact occurs around
        **{int(peak_hour):02d}:00 hours**, indicating a
        predictable temporal pattern suitable for proactive
        traffic enforcement planning.

        - These hotspots should receive priority
        patrolling, towing deployment and temporary
        parking restrictions.
        """
    )

    st.markdown("---")

    # ==================================================
    # DETAILED TABLES
    # ==================================================

    with st.expander(
            "📄 View Detailed Tables"
    ):

        st.subheader(
            "Junction Details"
        )

        st.dataframe(
            junction_df,
            use_container_width=True
        )

        st.subheader(
            "Police Station Details"
        )

        st.dataframe(
            station_df,
            use_container_width=True
        )

        st.subheader(
            "Hourly Details"
        )

        st.dataframe(
            hourly_df,
            use_container_width=True
        )