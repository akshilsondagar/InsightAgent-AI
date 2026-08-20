import json

from config.settings import OLLAMA_MODEL
from llm.client import get_ollama_client
from llm.prompts import build_recommendation_prompt

from models.recommendation import AIRecommendation


def _clean_json_response(content):
    """
    Clean JSON response returned by Ollama.
    """

    if not isinstance(content, str):
        raise ValueError(
            "Ollama response must be a string."
        )

    content = content.strip()

    # Remove markdown code blocks if present
    if content.startswith("```json"):
        content = content[len("```json"):].strip()

    elif content.startswith("```"):
        content = content[len("```"):].strip()

    if content.endswith("```"):
        content = content[:-3].strip()

    return content


def generate_recommendations(
    company_name,
    challenges,
    analysis
):
    """
    Generate AI-powered recommendations for the company.
    """

    prompt = build_recommendation_prompt(
        company_name=company_name,
        challenges=challenges,
        analysis=analysis
    )

    client = get_ollama_client()

    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    print("\n========== OLLAMA RESPONSE ==========")
    print(content)
    print("=====================================\n")

    content = _clean_json_response(content)

    try:
        data = json.loads(content)

    except json.JSONDecodeError as error:

        print("\n========== INVALID JSON ==========")
        print(content)
        print("==================================")

        raise ValueError(
            f"""
Ollama returned invalid JSON.

Error: {error}
Line: {error.lineno}
Column: {error.colno}
"""
        )

    recommendations_data = data.get(
        "recommendations",
        []
    )

    if not isinstance(recommendations_data, list):
        raise ValueError(
            "Ollama returned an invalid recommendations format."
        )

    recommendations = []

    for item in recommendations_data:

        if not isinstance(item, dict):
            continue

        recommendation = AIRecommendation(
            **item
        )

        recommendations.append(
            recommendation
        )

    return recommendations