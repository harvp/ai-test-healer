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


def suggest_fix(failure_message):
    # TEMPORARY MOCK for testing without hitting API
    return f"[MOCK FIX] Likely cause of failure: {failure_message.split(':')[1].strip()} (AI suggestion would go here)"
