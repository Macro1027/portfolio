import streamlit as st

from src.constant import info

# Footer
def display_footer():
    st.markdown(f'<div class="footer">Contact: {info["Email"]} </div>', unsafe_allow_html=True)
