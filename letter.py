import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="Birthday Letter ❤️",
    page_icon="💌",
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

        md = f"""
        <audio autoplay loop controls style="width:100%;">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """

        st.markdown(md, unsafe_allow_html=True)
    except:
        pass

autoplay_audio("neelothi.mp3")

# -----------------------------
# Header
# -----------------------------
st.markdown(
"""
<div class="glass">

<h1>💌 Happy Birthday My Shrii ❤️</h1>

<h3>15 July 2026 🎂</h3>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# -----------------------------
# Birthday Letter
# -----------------------------
st.markdown(
"""
<div class="glass">

<h2>To My Dearest Shrii ❤️</h2>

<p>

Happy Birthday, my love. 🎂❤️

Today is the most beautiful day because it marks the day the most wonderful person came into this world.

You are not just someone special to me—you are my happiness, my peace, my biggest blessing, and the reason behind countless smiles.

Every moment spent with you becomes a beautiful memory that I treasure deeply.

I hope this birthday fills your heart with endless joy, your life with success, and your days with love and laughter.

No matter what happens, I will always pray for your happiness and stand beside you whenever you need me.

Thank you for being the beautiful soul that lights up my world.

You deserve every wonderful thing this universe has to offer.

Never stop smiling, because your smile is my favorite sight.

Happy Birthday once again, my princess.

May all your dreams come true.

I love you today...

I love you tomorrow...

I will love you forever.

❤️❤️❤️

</p>

<h2>

Forever Yours,

❤️

</h2>

</div>
""",
unsafe_allow_html=True
)

st.write("")

# -----------------------------
# Birthday Wishes
# -----------------------------
st.markdown("## 🌹 Birthday Wishes")

wishes = [
    "🎂 May your smile shine brighter than the stars.",
    "💖 May every dream become reality.",
    "🌸 May your heart always stay happy.",
    "✨ May success follow you everywhere.",
    "💕 May our memories grow forever.",
    "🌎 You deserve every happiness in this world.",
    "❤️ Thank you for existing."
]

for wish in wishes:
    st.success(wish)

st.write("")

# -----------------------------
# Balloons
# -----------------------------
if st.button("🎈 Celebrate Birthday"):
    st.balloons()
    st.snow()

st.write("")

# -----------------------------
# Quote
# -----------------------------
st.info(
"""
"Every birthday of yours reminds me how lucky I am to have you in my life."

❤️ Happy Birthday ❤️
"""
)

st.write("")

# -----------------------------
# Navigation
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🏠 Home"):
        st.switch_page("app.py")

with col2:
    if st.button("🎁 Birthday Surprise"):
        st.switch_page("pages/2_🎁_Birthday_Surprise.py")

st.write("")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
"""
<div class="footer">

Made with ❤️ only for Shrii

15 July 2026

</div>
""",
unsafe_allow_html=True
)
