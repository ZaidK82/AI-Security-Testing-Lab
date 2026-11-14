
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("ERROR: GEMINI_API_KEY not found in .env")
    raise SystemExit(1)

try:
    client = genai.Client(api_key=api_key)

    # Use Google's recommended model for new users
    model_name = "gemini-3.5-flash-lite"

    print(f"Testing Gemini model: {model_name}")
    print("Sending test prompt...")

    response = client.models.generate_content(
        model=model_name,
        contents="Explain prompt injection in artificial intelligence in one sentence."
    )

    print("\nGEMINI API CONNECTION SUCCESSFUL")
    print("Model:", model_name)
    print("\nActual Gemini response:")
    print(response.text)

except Exception as error:
    print("\nGEMINI API TEST FAILED")
    print("Error type:", type(error).__name__)
    print("Error details:", str(error))
