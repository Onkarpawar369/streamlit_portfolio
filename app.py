import requests
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests
from PIL import Image

image = Image.open("Images/virtual_assitant.png")
st.set_page_config(layout="wide")


def load_css(filename):
    with open(filename) as f:
        st.markdown(f'<style>{f.read}</style>', unsafe_allow_html=True)


load_css("Style/style.css")


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


coder_lottie = load_lottie_url("https://lottie.host/9e638ad9-6bb3-417b-b287-d5a6f39e5538/FFifgdTYlu.json")
contact_lottie = load_lottie_url("https://lottie.host/2cfbcabd-ee08-4e49-8980-c75c4c9cf668/CYD4Db1383.json")

# st.write("##")
st.subheader(" Hey Guys, :wave:")
st.title("Welcome to my portfolio Website ")
st.write("""👋 Hi, I’m @Onkarpawar369
👀 I’m interested in python programming
🌱 I’m currently learning web developement
💞️ I’m looking to collaborate on website developement
📫 How to reach me onkar369pawar@gmail.com check out my portfolio on https://onkarpawar.s3.ap-south-1.amazonaws.com/index.html""")
st.write("---")
with st.container():
    selected = option_menu(menu_title=None, options=["About", "Projects", "Contacts"],
                           icons=['persone', 'code-slash', 'person-rolodex'], orientation='horizontal')

if selected == 'About':
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.subheader("I am Onkar Pawar,")
            st.title("Software Engineer at capgemini")
        with col2:
            st_lottie(coder_lottie)

        st.write("---")
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("""
            Experience
            - Capgemini
                2.4 years of experience""")
        with col4:
            st.subheader("""
            Experience
            - Capgemini
                2.4 years of experience""")

if selected == 'Projects':
    with st.container():
        st.subheader("Projects")
        st.write("---")
        col5, col6 = st.columns(2)
        with col5:
            st.image(image)
        with col6:
            st.subheader("Virtual Assistant Alexa")
            st.markdown("[Visit Github Repo]{https://github.com/Onkarpawar369/virtual_assistant_alexa}")
if selected == 'Contacts':
    st.header("Get in Touch!")
    st.write("##")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/onkar369pawar@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false>
     <input type="text" name="name" placeholder= "Your Name" required>
     <input type="email" name="email" placeholder= "Your Email" required>
     <textarea  name="message" placeholder= "Your Message" required></textarea>
     <button type="submit">Send</button>
    </form>"""
    leftcol, rightcole = st.columns((2, 1))
    with leftcol:
        st.markdown(contact_form, unsafe_allow_html=True)
    with rightcole:
        st_lottie(contact_lottie, height=300)
