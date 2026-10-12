from google import genai
from google.genai import types

from src.config import GEMINI_API_KEY, GEMINI_MODEL


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_response(
    messages: list[dict[str, str]],
    system_prompt: str,
) -> str:
    """Generate an answer using Gemini."""

    contents = []

    for message in messages:
        role = message.get("role")
        content = message.get("content", "").strip()

        if not content or role not in {"user", "assistant"}:
            continue

        contents.append(
            {
                "role": "user" if role == "user" else "model",
                "parts": [{"text": content}],
            }
        )

    if not contents:
        raise ValueError("No valid messages were provided.")

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.7,
        ),
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    return response.text.strip()