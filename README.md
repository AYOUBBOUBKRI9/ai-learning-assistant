# AI Learning Assistant

AI Learning Assistant is a conversational assistant designed
to support professional training and help users learn.

## Features

- Conversational interface powered by the Gemini API
- Prompt engineering for professional training
- Conversation history during the active session
- Streamlit web interface
- Error handling for API requests

## Architecture

User
  -> Streamlit interface
  -> Python application
  -> Gemini API
  -> Generated response

## Technologies

- Python
- Streamlit
- Google GenAI SDK
- Gemini API
- Git and GitHub

## Installation

1. Clone this repository.
2. Install the dependencies:

   pip install -r requirements.txt

3. Configure your Gemini API key as an environment variable.

Linux / macOS:

   export GEMINI_API_KEY="your_api_key"

Windows PowerShell:

   $env:GEMINI_API_KEY="your_api_key"

4. Start the application:

   streamlit run app.py

## Security

Never commit API keys, authentication tokens, or other secrets.
Store credentials in environment variables or a secret manager.

## Current limitations

- Conversation history is session-based.
- Responses depend on the availability and limits of the Gemini API.
- Persistent storage and document-based retrieval are not yet implemented.

## Future improvements

- Interactive quizzes and automatic correction
- Retrieval-Augmented Generation (RAG) with training documents
- Persistent conversation storage
- Automated tests and improved error handling
