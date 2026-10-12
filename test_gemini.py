from google import genai

from src.config import GEMINI_API_KEY, GEMINI_MODEL

client = genai.Client(api_key=GEMINI_API_KEY)

try:
    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents="Say hello in one short sentence.",
    )

    print("Gemini response:")
    print(response.text)

except Exception as error:
    print("Error type:", type(error).__name__)
    print("Error details:", error)