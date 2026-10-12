from src.llm import generate_response
from src.prompts import build_system_prompt


def initialize_chat(session_state) -> None:
    """Initialize conversation history."""

    if "messages" not in session_state:
        session_state.messages = []


def clear_chat(session_state) -> None:
    """Clear conversation history."""

    session_state.messages = []


def add_message(
    session_state,
    role: str,
    content: str,
) -> None:
    """Append a message to the conversation."""

    session_state.messages.append(
        {
            "role": role,
            "content": content,
        }
    )


def get_ai_response(
    session_state,
    subject: str,
    study_mode: str,
) -> str:
    """Generate an answer using the current conversation."""

    system_prompt = build_system_prompt(
        subject=subject,
        study_mode=study_mode,
    )

    return generate_response(
        messages=session_state.messages,
        system_prompt=system_prompt,
    )