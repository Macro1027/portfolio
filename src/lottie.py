import requests
import streamlit as st

class Lottie:
    def __init__(self):
        self.local_css("style/style.css")
        self.load_assets()
        self.generate_skills()
        

    def load_assets(self):
        # loading assets
        self.lottie_gif = self.load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
        self.python_lottie = self.load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
        self.java_lottie = self.load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
        self.my_sql_lottie = self.load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
        self.git_lottie = self.load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
        self.github_lottie = self.load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")

    def load_lottieurl(self, url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    def local_css(self, file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    
    def generate_skills(self):
        self.skills = [
            {'lottie': self.python_lottie, 'height': 70, 'width': 70, 'key': "python", 'speed': 2.5},
            {'lottie': self.java_lottie, 'height': 70, 'width': 70, 'key': "java", 'speed': 4},
            {'lottie': self.git_lottie, 'height': 70, 'width': 70, 'key': "git", 'speed': 2.5},
            {'lottie': self.github_lottie, 'height': 50, 'width': 50, 'key': "github", 'speed': 2.5},
        ]
        

