# 🚦 ParkSight AI
### Intelligent Parking-Induced Congestion Monitoring and Enforcement System

ParkSight AI is an AI-driven parking intelligence and congestion analytics platform designed to identify illegal parking hotspots, estimate their impact on urban traffic movement, and support data-driven traffic enforcement decisions.

The system transforms historical parking violation records into actionable intelligence by analysing spatial, temporal, and behavioural patterns of illegal parking incidents across Bengaluru. Through interactive dashboards and heatmaps, ParkSight AI enables traffic authorities to proactively identify high-risk locations, prioritise enforcement resources, and implement targeted interventions to reduce parking-induced congestion.

---

# 🎯 Problem Statement

Illegal parking is one of the major contributors to urban traffic congestion. Vehicles parked on carriageways, junctions, and no-parking zones reduce road capacity, obstruct traffic flow, and create significant delays during peak hours.

Traditional traffic management approaches are often reactive and rely heavily on manual monitoring. There is a need for an intelligent system capable of:

- Identifying recurring illegal parking hotspots
- Estimating the congestion impact of parking violations
- Detecting temporal congestion patterns
- Prioritising enforcement resources
- Supporting evidence-based traffic management decisions

ParkSight AI addresses these challenges by integrating data analytics, congestion scoring, geospatial visualisation, and interactive dashboards into a unified decision-support platform.

---

# 💡 Objectives

The primary objectives of ParkSight AI are:

- Analyse illegal parking incidents across Bengaluru
- Identify high-density parking violation hotspots
- Estimate congestion severity using a Congestion Impact Score (CIS)
- Discover spatial and temporal traffic patterns
- Prioritise locations requiring enforcement intervention
- Generate actionable recommendations for traffic authorities
- Provide interactive visual analytics for decision-makers

---

# 🏗 System Architecture

The system follows a modular analytics pipeline:
Parking Violation Dataset
↓
Data Cleaning & Preprocessing
↓
Feature Engineering
↓
Congestion Impact Score (CIS) Estimation
↓
Spatial & Temporal Analytics
↓
Hotspot Identification
↓
Interactive Visualisation Dashboard
↓
Enforcement Recommendations

---

# 📊 Dataset Information

The project uses historical parking violation records containing information such as:

- Violation Type
- Vehicle Type
- Date and Time of Violation
- Police Station Jurisdiction
- Junction Name
- Geographic Coordinates
- Congestion Indicators

### Analysis Period
**November 2023 – April 2024**

### Coverage
- 55 Police Stations
- 170 Junctions
- Nearly 300,000 parking violation records

---

# 🧠 Congestion Impact Score (CIS)

ParkSight AI introduces a custom metric called the **Congestion Impact Score (CIS)**.

The score estimates the extent to which an illegal parking incident contributes to traffic congestion by considering factors such as:

- Spatial characteristics
- Temporal patterns
- Incident frequency
- Junction-level severity
- Traffic behaviour indicators

The CIS enables incidents to be classified into different risk levels:

| Risk Level | Interpretation |
|------------|----------------|
| Low | Routine monitoring sufficient |
| Medium | Preventive patrolling recommended |
| High | Targeted enforcement required |
| Critical | Immediate intervention necessary |

---

# 🖥 Dashboard Modules

## 1️⃣ Overview Dashboard

Provides a high-level executive summary of parking intelligence.

Features:
- Total violations analysed
- Average Congestion Impact Score
- Police station and junction coverage
- Top parking violation categories
- Vehicle distribution analysis
- Daily congestion trend visualisation
- Key observations and insights

---

## 2️⃣ Interactive Heatmaps

Provides geospatial visualisation of illegal parking patterns.

Features:
- Illegal parking density heatmap
- Congestion impact heatmap
- Hour-wise parking hotspot visualisation
- Interactive maps for spatial exploration

The heatmaps help authorities identify:

- Persistent parking hotspots
- High-congestion zones
- Temporal changes in parking behaviour

---

## 3️⃣ Hotspots & Enforcement Prioritisation

Identifies locations requiring immediate attention.

Features:
- Top junction hotspots
- Top police station jurisdictions
- Congestion severity metrics
- Priority enforcement indicators
- Detailed hotspot tables

The module supports proactive resource deployment by identifying where enforcement actions can generate maximum congestion reduction.

---

## 4️⃣ AI-Driven Recommendations

Transforms analytical insights into operational decisions.

Features:
- Risk distribution analysis
- Priority enforcement zones
- Enforcement response matrix
- AI-generated recommendations
- Resource allocation guidance

Recommended actions include:

- Targeted patrolling
- Tow truck deployment
- Temporary no-parking enforcement
- Additional personnel allocation
- Continuous hotspot monitoring

---

# 📈 Visual Analytics

ParkSight AI incorporates multiple visualisation techniques:

- Interactive Plotly Charts
- Geographic Heatmaps
- Hotspot Rankings
- Risk Distribution Charts
- Congestion Trend Analysis
- Executive KPI Dashboards

The system focuses on transforming raw parking data into intuitive visual intelligence for decision-makers.

---

# 🛠 Technologies Used

### Programming Language
- Python

### Data Processing
- Pandas
- NumPy

### Data Visualisation
- Plotly
- Folium

### Dashboard Development
- Streamlit

### Geospatial Analytics
- Folium HeatMaps
- HTML-based Interactive Maps

---

# 📂 Project Structure

```text
ParkSight-AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── pages/
│   ├── overview.py
│   ├── heatmaps.py
│   ├── hotspots.py
│   └── recommendations.py
│
├── data/
│   └── parking_intelligence_with_cis.csv
│
├── outputs/
│   ├── junction_hotspots.csv
│   ├── station_summary.csv
│   └── hourly_risk.csv
│
├── assets/
│   ├── violation_heatmap.html
│   ├── cis_heatmap.html
│   └── hourly_heatmaps/
│       ├── hour_0.html
│       ├── hour_1.html
│       ├── ...
│       └── hour_23.html
```
# 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YamunaKalindi/ParkSight-AI.git
cd ParkSight-AI

pip install -r requirements.txt

streamlit run app.py

🎯 Expected Impact

ParkSight AI enables traffic authorities to move from reactive traffic management toward proactive, intelligence-driven enforcement.

The system assists in:

Reducing parking-induced congestion
Improving traffic flow efficiency
Prioritising enforcement resources
Identifying high-risk locations
Supporting evidence-based decision making
Enhancing urban mobility management
🔮 Future Enhancements

Potential extensions include:

Real-time parking violation ingestion
Live CCTV integration
Computer vision-based illegal parking detection
Predictive congestion forecasting
Reinforcement learning-based resource allocation
Mobile application for field officers
Automated alert and dispatch system
👩‍💻 Developed By

Yamuna B
B.Tech. Artificial Intelligence and Machine Learning
University Visvesvaraya College of Engineering (UVCE), Bengaluru

📜 License

This project has been developed for research purposes. The code and associated materials may be used for educational and non-commercial applications with appropriate attribution.

🚦 ParkSight AI

Transforming illegal parking data into actionable congestion intelligence for smarter and more efficient urban traffic enforcement.
