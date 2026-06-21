import streamlit as st
import pandas as pd

from overview import show_overview
from heatmaps import show_heatmaps
from hotspots import show_hotspots
from recommendations import show_recommendations


# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="ParkSight AI",
    page_icon="🚦",
    layout="wide"
)


# ==================================================
# LOAD DATA
# ==================================================

@st.cache_data
def load_data():

    df = pd.read_csv(
        "data/parking_intelligence_with_cis.csv"
    )

    junction_df = pd.read_csv(
        "outputs/junction_hotspots.csv"
    )

    station_df = pd.read_csv(
        "outputs/station_summary.csv"
    )

    hourly_df = pd.read_csv(
        "outputs/hourly_risk.csv"
    )

    return (
        df,
        junction_df,
        station_df,
        hourly_df
    )


df, junction_df, station_df, hourly_df = load_data()


# ==================================================
# SIDEBAR STYLING
# ==================================================

st.markdown(
    """
    <style>

    section[data-testid="stSidebar"] {
        background-color: #F8FAFC;
    }

    section[data-testid="stSidebar"] hr {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.markdown(
    """
    # 🚦 ParkSight AI

    Intelligent Parking Intelligence Platform
    """
)

st.sidebar.markdown("---")

st.sidebar.caption(
    """
    **Monitoring illegal parking patterns,
    estimating congestion impact,
    and enabling data-driven
    enforcement decisions.**
    """
)

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "",
    [
        "📊 Overview",
        "🗺️ Heatmaps",
        "🔥 Hotspots",
        "🚔 Recommendations"
    ]
)

st.sidebar.markdown("---")

st.sidebar.caption(
    f"""
    📅 Nov 2023 – Apr 2024

    🚗 {len(df):,} Violations

    🚦 Avg CIS: {df['cis'].mean():.2f}

    📍 {df['police_station'].nunique()} Police Stations

    🛣️ {df['junction_name'].nunique()} Junctions
    """
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Built using AI-driven parking intelligence and congestion analytics."
)


# ==================================================
# PAGE ROUTING
# ==================================================

if page == "📊 Overview":

    show_overview(
        df,
        junction_df,
        station_df,
        hourly_df
    )

elif page == "🗺️ Heatmaps":

    show_heatmaps()

elif page == "🔥 Hotspots":

    show_hotspots(
        junction_df,
        station_df,
        hourly_df
    )

elif page == "🚔 Recommendations":

    show_recommendations(
        df
    )