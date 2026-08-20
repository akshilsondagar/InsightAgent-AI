import json


def extract_json(response_text: str) -> dict:
    """
    Extract and parse JSON from an AI response.
    """

    response_text = response_text.strip()

    # Remove Markdown JSON code blocks if the model adds them
    if response_text.startswith("```json"):
        response_text = response_text[7:]

    elif response_text.startswith("```"):
        response_text = response_text[3:]

    if response_text.endswith("```"):
        response_text = response_text[:-3]

    response_text = response_text.strip()

    return json.loads(response_text)