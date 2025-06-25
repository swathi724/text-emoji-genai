
import streamlit as st
from transformers import pipeline

st.title("Text-to-Emoji Converter 🤖➡️😄")

st.write("Enter a sentence and get relevant emojis predicted using a Generative AI model.")

generator = pipeline("text-generation", model="gpt2")

# Emoji mapping (very simple mock-up for demo)
emoji_map = {
    "happy": "😄", "sad": "😢", "love": "❤️", "angry": "😠",
    "party": "🎉", "food": "🍕", "sleep": "😴", "money": "💰"
}

def generate_emojis(text):
    results = generator(text, max_length=30, num_return_sequences=1)
    prediction = results[0]["generated_text"]
    # Mocked scoring (in real use: tokenizer+emoji classifier)
    emojis = [v for k, v in emoji_map.items() if k in prediction.lower()]
    return emojis or ["🤔"]

user_input = st.text_input("Type your sentence here:")

if user_input:
    emojis = generate_emojis(user_input)
    st.markdown(f"### Suggested Emojis: {' '.join(emojis)}")
