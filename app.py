import streamlit as st
import streamlit.components.v1 as components
import random
import base64

st.set_page_config(
    page_title="Happy Birthday ❤️",
    page_icon="🎂",
    layout="centered"
)

# --------------------------
# Load CSS
# --------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# --------------------------
# Background Music
# --------------------------
def autoplay_audio(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    b64 = base64.b64encode(data).decode()

    md = f"""
    <audio autoplay loop controls style="width:100%;">
    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """

    st.markdown(md, unsafe_allow_html=True)

# --------------------------
# Loader
# --------------------------

with st.spinner("🎂 Preparing Your Birthday Surprise..."):
    import time
    time.sleep(3)

# --------------------------
# Music
# --------------------------

try:
    autoplay_audio("neelothi.mp3")
except:
    st.warning("Place neelothi.mp3 in project folder.")

# --------------------------
# Quotes
# --------------------------

quotes = [

"Happy Birthday to the Queen of my Heart ❤️",

"You are my favourite reason to smile 💖",

"You deserve every happiness in this world 🌎",

"Every birthday of yours is my favourite celebration 🎂",

"You are my sunshine on every cloudy day ☀️",

"My heart belongs only to you ❤️",

"You make every moment magical ✨",

"I'm lucky to celebrate another birthday with you 💕",

"Forever isn't enough with you ❤️",

"Happy Birthday My Princess 👑"

]

# --------------------------
# Header
# --------------------------

st.markdown(
"""
<div class="glass">

<h1>🎂 Happy Birthday Shrii ❤️</h1>

<h3>15 July 2026</h3>

<p>

Today isn't just another day.

Today is the day my favourite person entered this world.

</p>

</div>

""",
unsafe_allow_html=True
)

st.write("")

# --------------------------
# Buttons
# --------------------------

col1,col2=st.columns(2)

with col1:

    if st.button("💌 Birthday Letter"):

        st.switch_page("pages/1_💌_Birthday_Letter.py")

with col2:

    if st.button("🎁 Birthday Surprise"):

        st.switch_page("pages/2_🎁_Birthday_Surprise.py")

st.write("")

# --------------------------
# Random Quote
# --------------------------

if st.button("❤️ Click Me"):

    st.success(random.choice(quotes))

    st.balloons()

# --------------------------
# Footer
# --------------------------

st.markdown(
"""
<div class="footer">

Made with ❤️ only for Shrii

</div>
""",
unsafe_allow_html=True
)
