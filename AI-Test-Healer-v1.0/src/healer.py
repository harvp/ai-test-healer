# src/healer.py
import os
import re
from dotenv import load_dotenv

load_dotenv()

AI_MODE = os.getenv("AI_MODE", "mock").lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- Detect OpenAI SDK version and import accordingly ---
try:
    import openai
    version = getattr(openai, "__version__", "0.0.0")
    major_version = int(version.split(".")[0]) if re.match(r"\d+", version) else 0
except Exception:
    openai = None
    major_version = 0

client = None
if openai and major_version >= 1:
    # New 1.x+ SDK style
    try:
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)
    except Exception:
        client = None
elif openai and major_version < 1:
    # Old SDK style
    openai.api_key = OPENAI_API_KEY


# --- Prompt and mock fix helpers ---
def _generate_prompt(failure):
    """Format a compact, structured prompt for the LLM."""
    if isinstance(failure, dict):
        test_case = failure.get("Test Case", "Unknown test")
        error_message = failure.get("Error Message", "Unknown error")
    else:
        test_case = "Unknown test"
        error_message = str(failure)

    return (
        f"You are an expert in Katalon automated testing.\n"
        f"A test case named '{test_case}' failed with this message:\n"
        f"{error_message}\n\n"
        "Explain the most likely cause and suggest a fix in the Groovy test script.\n"
        "Keep your response short and practical."
    )


def _mock_fix(failure):
    """Return a mock suggestion when AI mode is off or unavailable."""
    if isinstance(failure, dict):
        error_message = failure.get("Error Message", "Unknown error")
    else:
        error_message = str(failure)
    reason = error_message.split(":")[0] if ":" in error_message else error_message[:80]
    return f"[MOCK FIX] Likely cause of failure: {reason.strip()} (AI suggestion would go here)"


# --- Main function ---
def suggest_fix(failure):
    """Suggest a fix for a test failure, adapting to SDK version and mode."""
    if AI_MODE == "mock" or not OPENAI_API_KEY:
        return _mock_fix(failure)

    prompt = _generate_prompt(failure)

    try:
        if client and major_version >= 1:
            # New SDK (v1+)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            return response.choices[0].message.content.strip()

        elif openai and major_version < 1:
            # Old SDK (v0.x)
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )
            return response.choices[0].message.content.strip()

        else:
            # Fallback
            return _mock_fix(failure)

    except Exception as e:
        return f"[ERROR: {type(e).__name__}] Using mock fallback — {_mock_fix(failure)}"
