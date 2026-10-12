
import os

from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.6-flash",
).strip()

if (
    not GEMINI_API_KEY
    or GEMINI_API_KEY == "PASTE_YOUR_GEMINI_API_KEY_HERE"
    or GEMINI_API_KEY == "your_gemini_api_key_here"
):
    raise RuntimeError(
        "GEMINI_API_KEY is missing. Add your key to the .env file."
    )

if not GEMINI_MODEL:
    raise RuntimeError(
        "GEMINI_MODEL is missing from the .env file."
    )
