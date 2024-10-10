import streamlit as st
import openai
from dotenv import load_dotenv
import os
import fitz  # PyMuPDF for PDF processing
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    st.error("API key not found. Please check your .env file.")

st.title("Mini Chat-Bot")
st.write("Upload File")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
st.markdown("Put YouTube video link below")
raw_transcript = st.text_input("Link")

# Set up session state for model and messages
if "openai_model" not in st.session_state:
    st.session_state.openai_model = "gpt-4o-mini"

if "messages" not in st.session_state:
    st.session_state.messages = []

# Extract YouTube transcript
parsed_url = urlparse(raw_transcript)
if parsed_url.query:
    video_id = parsed_url.query.split("=")[1]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        video_text = " ".join([content["text"] for content in transcript])
        st.session_state.messages.append({"role": "system", "content": video_text})

        if st.button("Summarize Video"):
            summarized_video = openai.ChatCompletion.create(
                model=st.session_state.openai_model,
                messages=[{"role": "user", "content": f"Summarize the following YouTube video content: {video_text}"}]
            )
            st.session_state.messages.append({"role": "assistant", "content": summarized_video.choices[0].message.content})
    except Exception as e:
        st.error(f"Error retrieving transcript: {e}")

# Extract text from uploaded PDF
if uploaded_file is not None:
    try:
        docs = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        pdf_text = "".join([page.get_text() for page in docs])
        st.session_state.messages.append({"role": "system", "content": pdf_text})

        if st.button("Summarize Text"):
            summarize_text = openai.ChatCompletion.create(
                model=st.session_state.openai_model,
                messages=[{"role": "user", "content": f"Summarize the following content: {pdf_text}"}]
            )
            st.session_state.messages.append({"role": "assistant", "content": summarize_text.choices[0].message.content})
    except Exception as e:
        st.error(f"Error processing PDF: {e}")

# Display conversation history
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chatbot interaction
if prompt := st.chat_input("Enter message here"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        response = openai.ChatCompletion.create(
            model=st.session_state.openai_model,
            messages=[{"role": msg["role"], "content": msg["content"]} for msg in st.session_state.messages]
        )
        response_content = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": response_content})

        with st.chat_message("assistant"):
            st.markdown(response_content)
    except Exception as e:
        st.error(f"Error with OpenAI response: {e}")

