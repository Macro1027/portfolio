import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline

from scripts.constant import *
from scripts.chatbot import Chatbot
from scripts.lottie import Lottie
st.set_page_config(page_title='Template' ,layout="wide",page_icon='👧🏻')

'''CUSTOMISE BIO.TXT'''

chatbot = Chatbot()
lottie = Lottie()
# -----------------  chatbot  ----------------- #
user_input = chatbot.chat()

# -----------------  loading assets  ----------------- #
def display_photo():
    st.sidebar.markdown(info['Photo'],unsafe_allow_html=True)

# ----------------- info ----------------- #
def display_info():
    with st.container():
        col1,col2 = st.columns([8,3])

        full_name = info['Full_Name']
        with col1:
            colour1 = '#FFD4DD'
            colour2 = '#000395'
            colour3 = 'e0fbfc'
            content1 = f"Hi, I'm {info['Full_Name']}👋"
            content2 = info["Intro"]
            st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{colour1}, {colour2});font-size:60px;border-radius:2%;">'
                        f'<span style="color:{colour3};">{content1}</span><br>'
                        f'<span style="color:white;font-size:17px;">{content2}</span></h1>', 
                        unsafe_allow_html=True)
            st.write("")
            st.write(info['About'])
            
            
        with col2:
            st_lottie(lottie.lottie_gif, height=280, key="data")
    
        

# ----------------- skillset ----------------- #
def display_skills(skills):
    with st.container():
        st.subheader('⚒️ Skills')
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        for i, skill in enumerate(skills):
            with [col1, col2, col3, col4][i % 4]:
                st_lottie(skill['lottie'], height=skill['height'], width=skill['width'], key=skill['key'], speed=skill['speed'])

    
    
# ----------------- timeline ----------------- #
def display_timeline():
    with st.container():
        st.markdown("""""")
        st.subheader('📌 Project snapshot')

        # load data
        with open('example.json', "r") as f:
            data = f.read()

        # render timeline
        timeline(data, height=400)


# MAIN
if __name__ == "__main__":
    skills = lottie.skills
    display_photo()
    display_skills(skills)
    display_info()
    display_timeline()