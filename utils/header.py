import streamlit as st

if __name__ == "__main__":
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