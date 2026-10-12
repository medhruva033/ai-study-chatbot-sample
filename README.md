# AI Study Chatbot

An AI-powered study assistant built with Python, Streamlit,
and the Google Gemini API.

## Features

- Conversational AI study tutor
- Multiple technical subjects
- Explain, Quiz Me, Interview, and Coding Problem modes
- Conversation history during the current session
- Clear conversation functionality
- Environment-based API key management
- Automated prompt tests

## Tech Stack

- Python
- Streamlit
- Google Gemini API
- Google GenAI Python SDK
- python-dotenv
- Pytest
- Git and GitHub

## Project Structure

```text
ai-study-chatbot/
├── app.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── llm.py
│   ├── prompts.py
│   └── chat.py
├── tests/
│   └── test_prompts.py
└── assets/
    └── screenshots/