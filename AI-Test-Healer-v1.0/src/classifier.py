# src/classifier.py
import re
from error_categroies import ERROR_CATEGORIES

def classify_failure(error_message):
    """
    Return the first matching error category for a failure message.
    If none match, return 'Unknown'.
    """
    for category in ERROR_CATEGORIES:
        if re.search(category["pattern"], error_message, re.IGNORECASE):
            return category
    return {
        "name": "Unknown",
        "description": "No known category matched",
        "ai_focus": ["Provide general troubleshooting suggestions"]
    }
