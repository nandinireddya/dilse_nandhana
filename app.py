import streamlit as st
from openai import OpenAI

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
        body {
            background-color: #fff8f9; /* soft blush pink background */
        }
        .main {
            background-color: #fff8f9;
            font-family: 'Poppins', sans-serif;
        }
        h1, h2, h3 {
            color: #b03060; /* rose red for headings */
        }
        .stTextInput > div > div > input {
            border: 2px solid #ff7ea5;
            border-radius: 10px;
            padding: 8px;
            background-color: #fff;
        }
        .stTextInput > div > div > input:focus {
            border-color: #ff1493;
            box-shadow: 0 0 5px #ff1493;
        }
        .stSuccess {
            background-color: #ffe6f0;
            border-radius: 10px;
            padding: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Dil Se Nandhana", page_icon="💖")

st.title("💖 Dil Se Nandhana")
st.subheader("Where Every Thread Speaks Emotion")

st.write("""
Welcome to *Dil Se Nandhana*, your one-stop store for elegant sarees and more.
Here you can chat with our AI assistant to explore collections, get styling ideas, and more!
""")

# --- OpenAI Setup ---
client = OpenAI(api_key = st.secrets["OPENAI_API_KEY"])

user_input = st.text_input("💬 Ask your AI stylist anything:")

if user_input:
    st.markdown(f"<p style='color:#b03060;font-weight:500;'>🧵 Our stylist is thinking about: <i>{user_input}</i></p>", unsafe_allow_html=True)
    with st.spinner("✨ Styling suggestions loading..."):
        try :
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a creative fashion stylist for Dil Se Nandhana."},
                    {"role": "user", "content": user_input}
                ]
            )
            reply = response.choices[0].message.content
            st.success(f"💖 {reply}")
        except Exception as e:
            st.error(f"error: {e}")
            
        
