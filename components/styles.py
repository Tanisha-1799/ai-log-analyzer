import streamlit as st


def load_css():

    st.markdown("""
    <style>

    /* ---------------------------------------------------
    MAIN LAYOUT
    --------------------------------------------------- */

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* ---------------------------------------------------
    EXECUTIVE SUMMARY CARD
    --------------------------------------------------- */

    .summary-card {
        padding: 1.5rem;
        border-radius: 16px;
        background: rgba(36, 41, 46, 0.75);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.5rem;
    }

    /* ---------------------------------------------------
    INCIDENT RIBBON
    --------------------------------------------------- */

    .incident-ribbon-high {
        padding: 1rem;
        border-radius: 12px;
        background: rgba(255, 75, 75, 0.12);
        border-left: 6px solid #ff4b4b;
        margin-bottom: 1rem;
        font-size: 1rem;
        font-weight: 600;
    }

    .incident-ribbon-medium {
        padding: 1rem;
        border-radius: 12px;
        background: rgba(255, 193, 7, 0.12);
        border-left: 6px solid #ffc107;
        margin-bottom: 1rem;
        font-size: 1rem;
        font-weight: 600;
    }

    .incident-ribbon-low {
        padding: 1rem;
        border-radius: 12px;
        background: rgba(40, 167, 69, 0.12);
        border-left: 6px solid #28a745;
        margin-bottom: 1rem;
        font-size: 1rem;
        font-weight: 600;
    }

    /* ---------------------------------------------------
    KPI CARDS
    --------------------------------------------------- */

    .kpi-card {
        padding: 1.4rem;
        border-radius: 18px;
        background-color: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        text-align: center;
        margin-bottom: 1rem;
    }

    .kpi-title {
        font-size: 0.95rem;
        opacity: 0.75;
        margin-bottom: 0.7rem;
    }

    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
    }

    /* ---------------------------------------------------
    ANALYSIS CARDS
    --------------------------------------------------- */

    .analysis-card {
        padding: 1.4rem;
        border-radius: 14px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        margin-bottom: 1.2rem;
    }

    .analysis-title {
        font-size: 1.1rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
    }

    /* ---------------------------------------------------
    SECTION HEADINGS
    --------------------------------------------------- */

    h2 {
        margin-top: 1rem;
        margin-bottom: 1rem;
    }

    h3 {
        margin-top: 0;
        margin-bottom: 0.8rem;
    }

    /* ---------------------------------------------------
    EXPANDERS
    --------------------------------------------------- */

    .streamlit-expanderHeader {
        font-size: 1rem;
        font-weight: 600;
    }

    /* ---------------------------------------------------
    SMALL TEXT
    --------------------------------------------------- */

    .small-muted {
        opacity: 0.7;
        font-size: 0.9rem;
    }

    /* ---------------------------------------------------
    DIVIDER SPACING
    --------------------------------------------------- */

    hr {
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    </style>
    """, unsafe_allow_html=True)