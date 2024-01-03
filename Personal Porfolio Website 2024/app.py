from email.mime import image
import re
import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tade:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use Local CSS


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)


local_css("style/style.css")

# LOAD ASSESTS
lottie_coding = load_lottieurl(
    "https://assets8.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")

img_project1 = Image.open(
    "/Users/user/Desktop/Personal Porfolio Website 2024/images/360_F_507584110_KNIfe7d3hUAEpraq10J7MCPmtny8EH7A.jpeg")
img_project2 = Image.open(
    "/Users/user/Desktop/Personal Porfolio Website 2024/images/360_F_507584110_KNIfe7d3hUAEpraq10J7MCPmtny8EH7A.jpeg")
img_project3 = Image.open(
    "/Users/user/Desktop/Personal Porfolio Website 2024/images/IMG_0211.jpg")
# Header Section
with st.container():
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project3)
    st.subheader("Hi, I'm Cesar :wave:")
    st.title("An Asparing Backend Developer")
    st.write("Detail-oriented Operations Analyst with 5 years of experience in the financial service industry and a zest for solving problems. Seeking to break into the Tech industry by leveraging my existing experience and new skills obtained with completing NuCamp's Back End, SQL, and DevOps with Python coding bootcamp and several projects")
    st.write("More About Me > (https://www.linkedin.com/in/cesar-marty-/)")

    st.write(
        "Bootcamp details here > (https://www.nucamp.co/bootcamp-overview/back-end-sql-devops-python)")

# WHAT I DO
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Skills & Qualifications")
        st.write("##")
        st.write("""
            - Design and use relational databases with SQL (Structured Query Language).
            - Link PostgreSQL databases to Python applications, creating powerful back end systems to handle complex data with ease.
            - SDLC 
            - CI/CD
            - Python
            - AWS
            - Flask and Django

        """)


with right_column:
    st_lottie(lottie_coding, height=300, key="coding")

# PROJECTS SECTION

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project1)
    with text_column:
        st.subheader("Title of Project")
        st.write(""" Description of Project, link to Github etc... 
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        
        """)
st.write("###")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_project2)
    with text_column:
        st.subheader("Title of Project")
        st.write(""" Description of Project, link to Github etc...
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        
        """)


# CONTANCT FORM
with st.container():
    st.write("---")
    st.header("Get in Touch With Me!")
    st.write("##")

    contact_form = """
<form action = "https://formsubmit.co/cesar.marty11@gmail.com" method = "POST" >
    <input type="hidden" name="_captcha" value="false">
    <input type = "text" name = "name" placeholder="Your name" required >
    <input type = "email" name = "email" placeholder="Your email" required >
    <textarea name="message" placehoder="Your message here" required></textarea>
    <button type = "submit" > Send </button>
</form >

"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
