
# Smart Chatbot for Summarization

This project is an AI-powered chatbot using GPT-4o Mini, designed to summarize PDF files and YouTube video transcripts. The chatbot provides concise insights, making content easier to understand.

## Features
- Summarize text from uploaded PDF files.
- Extract and summarize transcripts from YouTube videos.
- Interactive chatbot for user queries.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Git

### 1. Clone the Repository
```bash
git clone [https://github.com/ASD-Are/MachineLearning](https://github.com/ASD-Are/MachineLearning/tree/main/chatgpt/Use%20ChatGPT%20to%20create%20customer%20support%20website%20-%20data%20source%20web%20pages)
cd smart_chatbot
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

### 3. Install Dependencies
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Set Up API Key
Create a `.env` file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key
```
Replace `your_openai_api_key` with your actual OpenAI API key.

### 5. Run the Application
Start the Streamlit app:
```bash
streamlit run chatbot.py
```
Open the provided URL (typically `http://localhost:8501`) in your browser to access the chatbot interface.

## Using the Chatbot
1. **Upload a PDF**: Use the "Choose a PDF file" button to upload a document, then click "Summarize PDF" to get a summary.
2. **Summarize a YouTube Video**: Enter the video link, click "Summarize Video" to generate a summary of the transcript.
3. **Chat with the Bot**: Use the input box to interact with the AI chatbot for more queries or information.

## Example Output
- **PDF Summary**: See a concise version of the PDF content.
- **YouTube Summary**: Get a summarized version of the video transcript.
- **Chatbot Interaction**: Direct answers to your queries based on the uploaded content.

## Screenshot
Include a screenshot of the app interface here:
![App Screenshot](https://github.com/user-attachments/assets/4eca3f33-5799-4d0a-af57-6e474a32119c)
![image](https://github.com/user-attachments/assets/fc934c20-793c-4921-b42d-2e878a119dc9)\
![image](https://github.com/user-attachments/assets/cf82bdc3-f4e2-4d1e-b917-c85bf6f69b19)


## References
- [OpenAI API Documentation](https://platform.openai.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [YouTube Transcript API](https://pypi.org/project/youtube-transcript-api/)
- [PyMuPDF Documentation](https://pymupdf.readthedocs.io/)

## Known Issues
- Transcript extraction may fail if the YouTube video lacks captions.
- Large PDF files might take time to process.

## Future Enhancements
1. **Multilingual Support**: Summarize content in various languages.
2. **Mobile App Version**: Make the chatbot available as a mobile app.
3. **Enhanced UI**: Add features like dark mode and more flexible input methods.

## Appendix
[Google Slide](https://docs.google.com/presentation/d/12b1PPjLq-hRroUPZ66VEGLNbTz1yLyWTb2Jn84AZ2LE/edit?usp=sharing)
[Documentation with Screenshots of process and result](https://github.com/ASD-Are/MachineLearning/blob/main/chatgpt/Use%20ChatGPT%20to%20create%20customer%20support%20website%20-%20data%20source%20web%20pages/CS565_week3_HW2_Q2_20073_Aron_Dagniew.pdf)

