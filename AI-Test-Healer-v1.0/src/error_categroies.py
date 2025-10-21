# src/error_categories.py

ERROR_CATEGORIES = [
    {
        "name": "ElementNotFound",
        "pattern": r"(Web element .* not found|WebElementNotFoundException)",
        "description": "Missing element locator in the UI",
        "ai_focus": [
            "Check if XPath or CSS selector is stale",
            "Add waits or visibility checks",
            "Detect iframe or modal blocking element"
        ]
    },
    {
        "name": "NotVisible",
        "pattern": r"(is NOT visible)",
        "description": "Element is present but hidden",
        "ai_focus": [
            "Suggest WebUI.scrollToElement()",
            "Add waits or check conditional UI states"
        ]
    },
    {
        "name": "TextMismatch",
        "pattern": r"(Actual text .* and expected text .* are NOT matched)",
        "description": "Text assertion mismatch",
        "ai_focus": [
            "Normalize whitespace",
            "Suggest contains() or pattern matching instead of strict equals",
            "Recommend updated expected values if pattern drift detected"
        ]
    },
    {
        "name": "ConnectionError",
        "pattern": r"(Connection refused|timeout|network)",
        "description": "Network or environment failure",
        "ai_focus": [
            "Recommend retry logic",
            "Check environment health",
            "Classify as infrastructure vs test failure"
        ]
    },
    {
        "name": "RepositoryError",
        "pattern": r"(Object Repository/|repository path error)",
        "description": "Object Repository or path mismatch",
        "ai_focus": [
            "Resync or revalidate repository objects",
            "Detect broken object paths automatically"
        ]
    },
    {
        "name": "FrameworkException",
        "pattern": r"(WebElementNotFoundException|com.kms.katalon.core.*Exception)",
        "description": "Unhandled Selenium/Katalon internal failure",
        "ai_focus": [
            "Suggest try/catch",
            "Add robust retry logic"
        ]
    }
]
