import streamlit as st
import streamlit.components.v1 as components
import os


def show_heatmaps():

    st.title(
        "🗺️ Interactive Parking Heatmaps"
    )

    st.markdown(
        """
        Visual analytics for understanding the geographical
        distribution of illegal parking incidents and their
        estimated congestion impact across Bengaluru.
        """
    )

    st.markdown("---")

    # ====================================================
    # OVERALL HEATMAPS
    # ====================================================

    st.header(
        "Overall Spatial Patterns"
    )

    st.markdown(
        """
        The maps below provide a city-wide view of parking violations
        and their estimated traffic impact.

        The left map shows where illegal parking incidents are concentrated,
        while the right map highlights regions experiencing higher
        Congestion Impact Scores (CIS).
        """
    )

    c1, c2 = st.columns(2)

    # ====================================================
    # VIOLATION HEATMAP
    # ====================================================

    with c1:

        st.subheader(
            "📍 Illegal Parking Density"
        )

        st.caption(
            """
            Brighter regions indicate recurring illegal parking hotspots
            requiring increased monitoring and enforcement.
            """
        )

        violation_path = (
            "assets/violation_heatmap.html"
        )

        if os.path.exists(
                violation_path
        ):

            with open(
                    violation_path,
                    "r",
                    encoding="utf-8"
            ) as f:

                html = f.read()

            components.html(
                html,
                height=600,
                scrolling=False
            )

        else:

            st.warning(
                "Violation heatmap not found."
            )

    # ====================================================
    # CIS HEATMAP
    # ====================================================

    with c2:

        st.subheader(
            "🚦 Congestion Impact Score"
        )

        st.caption(
            """
            Higher intensity regions indicate locations where
            illegal parking is estimated to generate greater
            traffic disruption and congestion impact.
            """
        )

        cis_path = (
            "assets/cis_heatmap.html"
        )

        if os.path.exists(
                cis_path
        ):

            with open(
                    cis_path,
                    "r",
                    encoding="utf-8"
            ) as f:

                html = f.read()

            components.html(
                html,
                height=600,
                scrolling=False
            )

        else:

            st.warning(
                "CIS heatmap not found."
            )

    st.markdown("---")

    # ====================================================
    # HOURLY HEATMAPS
    # ====================================================

    st.header(
        "🕒 Hourly Hotspot Evolution"
    )

    st.markdown(
        """
        Illegal parking patterns are not constant throughout the day.

        Use the slider below to observe how parking hotspots evolve
        over a 24-hour period and identify time windows requiring
        targeted enforcement deployment.
        """
    )

    hour = st.slider(
        "Select Hour of Day",
        min_value=0,
        max_value=23,
        value=8,
        format="%d"
    )

    st.caption(
        f"Displaying hotspots for {hour:02d}:00 hours"
    )

    # ====================================================
    # CORRECT FILE NAME
    # ====================================================

    hourly_file = (
        f"assets/hourly_heatmaps/"
        f"hour_{hour}.html"
    )

    if os.path.exists(
            hourly_file
    ):

        with open(
                hourly_file,
                "r",
                encoding="utf-8"
        ) as f:

            html = f.read()

        components.html(
            html,
            height=700,
            scrolling=False
        )

        st.markdown(
            f"""
            #### Interpretation

            The above heatmap represents the spatial distribution of
            illegal parking incidents around **{hour:02d}:00 hours**.

            Persistent hotspots appearing across multiple time periods
            indicate regions requiring continuous enforcement attention,
            while temporary spikes may suggest time-specific parking
            management challenges.
            """
        )

    else:

        st.info(
            f"""
            No heatmap was generated for
            **{hour:02d}:00 hours**.

            This generally indicates insufficient incidents for that
            particular time window.
            """
        )

    st.markdown("---")

    # ====================================================
    # ACTIONABLE INSIGHTS
    # ====================================================

    st.subheader(
        "💡 Why These Heatmaps Matter"
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "📍 Spatial Analysis",
            "Hotspot Detection"
        )

        st.caption(
            """
            Identify persistent illegal parking clusters.
            """
        )

    with c2:

        st.metric(
            "🕒 Temporal Analysis",
            "Hourly Evolution"
        )

        st.caption(
            """
            Understand how congestion patterns change
            throughout the day.
            """
        )

    with c3:

        st.metric(
            "🚔 Decision Support",
            "Targeted Enforcement"
        )

        st.caption(
            """
            Prioritise patrol deployment and
            traffic intervention resources.
            """
        )