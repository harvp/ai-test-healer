# src/healer.py
import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

##def suggest_fix(failure_message):
##    prompt = f"""
##    The following test failed in an automated UI test:
##    "{failure_message}"
##    Explain what likely caused this failure and how to fix it in the script.
##    """
##    response = openai.ChatCompletion.create(
##        model="gpt-4o-mini",
##        messages=[{"role": "user", "content": prompt}],
##    )
##    return response.choices[0].message.content.strip()


def suggest_fix(failure):
    """
    Generate a mock AI suggestion for a given failure.
    Accepts either a string (legacy) or a dict with 'Error Message'.
    """
    # Handle both old and new formats
    if isinstance(failure, dict):
        error_message = failure.get("Error Message", "Unknown error")
    else:
        error_message = str(failure)

    # Try to extract a short reason from the message
    reason = error_message.split(":")[0] if ":" in error_message else error_message[:80]

    return f"[MOCK FIX] Likely cause of failure: {reason.strip()} (AI suggestion would go here)"

