import streamlit as st
import openai
from openai import OpenAI
st.set_page_config(page_title="Mood2Fit", page_icon="💋")
st.title("💋 Mood2Fit - Your AI Stylist")
st.write("Get outfit inspiration based on your **mood**, **event**, or **song**.")

# Fields
mood = st.text_input("💭 How are you feeling?")
event = st.text_input("📍 What's the occasion?")
song = st.text_input("🎵 Song you're vibing to")

openai_api_key = st.text_input("🗝️ Enter your OpenAI API Key", type = "password")

if st.button("✨ Generate Look"):
    if not openai_api_key:
        st.error("Please enter your OpenAI API key.")
    else:
        client = OpenAI(api_key=openai_api_key)
        prompt = f"""
        You are a highly creative, emotionally intelligent AI Fashion stylist call Mood2Fit.
        Your job is to create a personalised outfit based on someone's vibe- mood, event or a song.

        Instructions:
        1. Read the mood, event and song below.
        2. Think of a feeling this combo evokes - what kind of aesthetic, colors, textures and silhuoettes it inspires.
        3. Describe a moodboard in 2-3 sentences.
        4. Suggest a full outfit : top, bottom, shoes, accessories.
        5. Add makeup and hair suggestions that vibe with the look.Be inclusive
        6. Give 1 ✨Styling Tip✨ that elevates the look.
        7. Make it sound creative and totally wearable.Keep the tone fashion-foward, like something you'd see or hear on Tiktok.

        Inputs:
        Mood: {mood}
        Event: {event}
        Song: {song}
        """
        try:
            response = client.chat.completions.create(
                model = "gpt-4",
                messages = [{"role": "user", "content": prompt}],
                temperature = 0.8,
                max_tokens = 600
            )

            outfit = response.choices[0].message.content
            st.markdown("### 💋 Your Look:" )
            st.write(outfit)

        except Exception as e:
             st.error(f"Something went wrong: {e}")
  
