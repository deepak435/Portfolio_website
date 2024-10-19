import streamlit as st
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


col1, col2 = st.columns(2)

with col1:
    st.subheader("Hi :wave:")
    st.title("I am Venkata Deepak")

with col2:
    st.image("images/Deepakpic.png")

st.title(" ")


persona = """You are Deepak AI bot. You help people answer questions your self(i.e. Deepak)
    Answer as if you are responding. dont answer in second or third person.
    If you don't know they answer you simply say "That's a secret"
    Here is more info about Deepak:

    I am Venkata Deepak Ramisetty, a BTech student specializing in Artificial Intelligence and Machine Learning at PACE Institute of Technology & Sciences.
    I am passionate about data science, machine learning, and developing solutions that drive efficiency and innovation.
    With hands-on experience in data visualization, machine learning projects, and proficiency in Python, SQL, and key libraries like NumPy and Pandas, I am eager to contribute to impactful projects and grow my expertise further."""

st.title("Deepak's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK",use_container_width=400):
    prompt = persona +"Here is the question that the user ask" + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube Channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 250k+ Subscribers")
    st.write("- Over 150 Free Tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")

with col2:
    st.video("https://youtu.be/BFlRmIvqwSA")

st.title(" ")

st.title("My Setup")
st.image("images/setup.jpg")

st.write(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 70)
st.slider("Teaching", 0, 100, 85)
st.slider("Robotics", 0, 100, 75)

st.write(" ")
st.title("Gallery")

col1 , col2, col3 = st.columns(3)

with col1:
    st.image("images/g1.png")
    st.image("images/g2.jpg")
    st.image("images/g3.jpg")

with col2:
    st.image("images/g4.jpg")
    st.image("images/g5.jpg")
    st.image("images/g6.jpg")

with col3:
    st.image("images/g7.jpg")
    st.image("images/g8.jpg")
    st.image("images/g9.png")

st.subheader(" ")
st.write("CONTACT")
st.title("For any inquiries, email at")
st.subheader("contact@deepakramisetty43.com")