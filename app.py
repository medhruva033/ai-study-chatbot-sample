
import streamlit as st

from src.chat import (
    add_message,
    clear_chat,
    get_ai_response,
    initialize_chat,
)
from src.prompts import STUDY_MODES, SUBJECTS


# Page configuration
st.set_page_config(
    page_title="AI Study Chatbot",
    page_icon="🎓",
    layout="wide",
)


# Initialize conversation
initialize_chat(st.session_state)


# Sidebar
with st.sidebar:
    st.title("🎓 AI Study Chatbot")

    st.write(
        "Your AI-powered assistant for learning "
        "technical subjects and preparing for interviews."
    )

    st.divider()

    subject = st.selectbox(
        "📚 Select Subject",
        SUBJECTS,
    )

    study_mode = st.selectbox(
        "🎯 Study Mode",
        STUDY_MODES,
    )

    st.divider()

    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True,
    ):
        clear_chat(st.session_state)
        st.rerun()

    st.caption("Powered by Google Gemini")


# Main content
st.title("🎓 AI Study Chatbot")

st.write(
    "Learn DSA, DBMS, Operating Systems, Computer Networks, "
    "OOP, and more with your AI study tutor."
)

st.caption(f"Subject: {subject} · Mode: {study_mode}")


# Display conversation history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# User input
user_input = st.chat_input("Ask your study question...")


if user_input:
    user_input = user_input.strip()

    if user_input:
        add_message(
            st.session_state,
            "user",
            user_input,
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = get_ai_response(
                        st.session_state,
                        subject=subject,
                        study_mode=study_mode,
                    )

                    st.markdown(answer)

                    add_message(
                        st.session_state,
                        "assistant",
                        answer,
                    )

                except Exception as error:
                    st.error("Unable to generate a response.")

                    st.caption(
                        f"Error type: {type(error).__name__}"
                    )

                    # Show the full error for debugging.
                    st.code(str(error))

