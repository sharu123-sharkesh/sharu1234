import streamlit as st
import random
import base64
import time
from pathlib import Path

st.set_page_config(
    page_title="Birthday Surprise ❤️",
    page_icon="🎁",
    layout="centered"
)

# -----------------------------
# Load CSS
# -----------------------------
css_file = Path("style.css")
if css_file.exists():
    with open(css_file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Background Music
# -----------------------------
def autoplay_audio(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        b64 = base64.b64encode(data).decode()

        st.markdown(
            f"""
            <audio autoplay loop controls style="width:100%;">
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """,
            unsafe_allow_html=True,
        )
    except:
        pass

autoplay_audio("neelothi.mp3")

# -----------------------------
# Title
# -----------------------------
st.markdown("""
<div class="glass">
<h1>🎁 Birthday Surprise ❤️</h1>
<h3>15 July 2026</h3>
<p>A little surprise made only for you 💖</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Countdown Animation
# -----------------------------
st.subheader("✨ Ready?")

placeholder = st.empty()

for i in [3, 2, 1]:
    placeholder.markdown(
        f"<h1 style='text-align:center;font-size:80px;color:white'>{i}</h1>",
        unsafe_allow_html=True,
    )
    time.sleep(1)

placeholder.empty()

st.balloons()

# -----------------------------
# Love Quotes
# -----------------------------
quotes = [
    "❤️ Happy Birthday to the love of my life.",
    "🌹 Every heartbeat of mine whispers your name.",
    "💖 You are my biggest blessing.",
    "🎂 Every birthday of yours is my favorite celebration.",
    "💕 My happiest place is wherever you are.",
    "🌸 Thank you for making my life beautiful.",
    "✨ Your smile lights up my entire world.",
    "💝 I wish you endless happiness and love.",
    "👑 You'll always be my princess.",
    "❤️ Forever starts with you."
]

st.subheader("💌 Pick a Surprise Quote")

if st.button("❤️ Show My Surprise"):
    st.success(random.choice(quotes))
    st.balloons()

# -----------------------------
# Special Birthday Message
# -----------------------------
st.write("")

st.markdown("""
<div class="glass">

<h2>💖 A Special Message 💖</h2>

<p>

Today isn't just your birthday.

It's the day the world received its most beautiful gift.

Thank you for filling my life with laughter,
love,
hope,
and happiness.

I don't need thousands of reasons to smile.

I only need you.

May your life always be filled with

❤️ Happiness

🌸 Peace

🎂 Cake

✨ Success

💕 Love

and countless beautiful memories.

Happy Birthday once again.

I love you more than words can ever express.

</p>

<h2>❤️ Forever Yours ❤️</h2>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Memory Timeline
# -----------------------------
st.write("")
st.subheader("📅 Our Beautiful Journey")

timeline = [
    ("💖", "You entered my life."),
    ("😊", "You became my happiness."),
    ("❤️", "You became my home."),
    ("🎂", "15 July 2026 - Celebrating YOU."),
    ("♾️", "Forever together.")
]

for icon, text in timeline:
    st.info(f"{icon} {text}")

# -----------------------------
# Reasons I Love You
# -----------------------------
st.write("")
st.subheader("💝 10 Reasons I Love You")

reasons = [
    "Your beautiful smile 😊",
    "Your caring heart ❤️",
    "Your kindness 🌸",
    "Your laugh 😄",
    "Your eyes 👀",
    "The way you support me 💕",
    "Your honesty 🤍",
    "You make every day brighter ☀️",
    "You understand me 🫶",
    "Simply because you're YOU ❤️"
]

for reason in reasons:
    st.success(reason)

# -----------------------------
# Birthday Celebration Button
# -----------------------------
st.write("")

if st.button("🎉 Celebrate"):
    st.balloons()
    st.snow()
    st.success("🎂 Happy Birthday My Shrii ❤️")

# -----------------------------
# Final Message
# -----------------------------
st.write("")

st.markdown("""
<div class="glass">

<h1>🎂 Happy Birthday ❤️</h1>

<h2>15 July 2026</h2>

<p>

May this birthday become one of the happiest days of your life.

May every dream come true.

May every smile stay forever.

May every prayer be answered.

And may our story continue forever.

I Love You ❤️

</p>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# Navigation
# -----------------------------
st.write("")

col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("💌 Birthday Letter"):
        st.switch_page("pages/1_💌_Birthday_Letter.py")

# -----------------------------
# Footer
# -----------------------------
st.write("")

st.markdown("""
<div class="footer">

Made with ❤️ only for Shrii

15 July 2026

🎂 Happy Birthday 🎂

</div>
""", unsafe_allow_html=True)
