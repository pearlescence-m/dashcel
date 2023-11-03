import streamlit as st
from openpyxl import load_workbook

st.set_page_config(
    page_title="dashcel",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'mailto:meruyert.alimaganbetova@gmail.com',
        'Report a bug': "mailto:meruyert.alimaganbetova@gmail.com",
        'About': "# dashcel project is licensed under the Apache License, Version 2.0 (c) 2023"
    }
)

st.markdown("# 📊 dashcel")
st.markdown("---")

st.markdown("##### A cross-platform desktop application for automatic Excel-to-Python dashboard conversion.")
st.markdown("The primary philosophy when designing this tool was to reduce the amount of manual work that is spent in every \
            organization on converting existing data flows and reports in Excel to a more interactive and automatically updated \
            dashboards in Python. ")
st.markdown("---")
