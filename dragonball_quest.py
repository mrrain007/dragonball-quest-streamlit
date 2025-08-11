import streamlit as st
from PIL import Image
import random

# --- Game Data ---
characters = {
    "Goku": {
        "image": "https://static.wikia.nocookie.net/dragonball/images/7/76/Goku.png",
        "desc": "The Saiyan raised on Earth, always striving to get stronger."
    },
    "Vegeta": {
        "image": "https://static.wikia.nocookie.net/dragonball/images/2/2e/Vegeta.png",
        "desc": "The proud Prince of all Saiyans, always seeking a challenge."
    },
    "Gohan": {
        "image": "https://static.wikia.nocookie.net/dragonball/images/3/3b/Gohan.png",
        "desc": "Goku's son, gentle at heart but fierce in battle."
    },
    "Piccolo": {
        "image": "https://static.wikia.nocookie.net/dragonball/images/2/2e/Piccolo_Dragon_Ball.png",
        "desc": "The wise and powerful Namekian."
    }
}

quests = [
    "Fight against Frieza on Namek!",
    "Defend Earth from Majin Buu!",
    "Train in the Hyperbolic Time Chamber!",
    "Search for the Dragon Balls!",
    "Compete in the World Martial Arts Tournament!"
]

outcomes = [
    "You achieved victory! The world is safe.",
    "You barely escaped with your life. Try again!",
    "You powered up to a new level!",
    "You met a new ally who will help you on your journey.",
    "You were defeated, but your spirit remains strong."
]

# --- App UI ---
st.set_page_config(page_title="Dragon Ball Quest", page_icon="🐉")

st.title("🐉 Dragon Ball Quest")
st.markdown("Welcome to **Dragon Ball Quest!** Begin your adventure in the Dragon Ball universe.")

# Character Selection
character = st.selectbox("Choose your character:", list(characters.keys()))

if character:
    st.image(characters[character]["image"], width=200)
    st.info(characters[character]["desc"])

# Quest Start
if st.button("Start Quest!"):
    quest = random.choice(quests)
    st.subheader(f"Quest: {quest}")
    st.write("You set out bravely...")

    outcome = random.choice(outcomes)
    st.success(outcome)
    st.balloons()

st.markdown("---")
st.caption("Created with ❤️ using Streamlit. Fan project for demonstration purposes.")
