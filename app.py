import streamlit as st

st.title("My First App 😎🥕 by Cloudblitz")
st.image("krishna.gif")



import streamlit as st
from streamlit_lottie import st_lottie
import requests
import base64

# Set page configuration
st.set_page_config(page_title="Techno Game Music Player", page_icon="🎵", layout="centered")

# Title and description
st.title("🎮 Techno Game Music Player")
st.write("Press play to enjoy some energizing techno game music!")

# Add a relevant image/gif
# Using a placeholder URL for a techno music animation
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Using a music/techno related Lottie animation
lottie_music = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_bisdfwiv.json")

if lottie_music:
    st_lottie(lottie_music, height=200)
else:
    # Fallback image if Lottie doesn't load
    st.image("game.jpg", caption="Techno Music Vibes")

# Audio file (using base64 encoding for a small audio sample)
# Note: For a real app, you would link to an audio file URL or upload a file

# Since we can't include large audio files here, we'll use a placeholder
# In a real implementation, you would have an actual audio file
audio_file = None  # Placeholder

# Upload audio or use default
uploaded_file = st.file_uploader("Upload a techno music file", type=["mp3", "wav"])

if uploaded_file is not None:
    # Play the uploaded audio file
    st.audio(uploaded_file, format='audio/mp3')
    st.success("Playing your techno track! 🎧")
elif audio_file is None:
    # Provide a sample audio URL (replace with a real techno track URL)
    sample_audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    st.write("Using a sample track:")
    st.audio(sample_audio_url)
    st.info("Sample techno-inspired music playing 🎵")

# Add some styling
st.markdown("""
<style>
.stApp {
    background-color: #0a0a0a;
    color: #f0f0f0;
}
</style>
""", unsafe_allow_html=True)

# Footer
st.write("---")
st.write("Made with ❤️ for techno music lovers")
