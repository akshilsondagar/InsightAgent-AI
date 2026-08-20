import json

from config.settings import OLLAMA_MODEL
from llm.client import get_ollama_client
from llm.prompts import build_scoring_prompt

from models.scored_recommendation import ScoredRecommendation


def clean_json_response(content: str) -> str:
    """
    Clean Ollama JSON response.
    """

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:].strip()

    elif content.startswith("```"):
        content = content[3:].strip()

    if content.endswith("```"):
        content = content[:-3].strip()

    return content


def score_recommendations(
    company_name,
    recommendations
):
    """
    Score generated AI recommendations.
    """

    if not recommendations:
        return []

    # Convert recommendations into normal dictionaries
    recommendations_data = []

    for recommendation in recommendations:

        if hasattr(recommendation, "model_dump"):
            recommendations_data.append(
                recommendation.model_dump()
            )
        else:
            recommendations_data.append(
                recommendation
            )

    # Build prompt
    prompt = build_scoring_prompt(
        company_name=company_name,
        recommendations=recommendations_data
    )

    # Get Ollama client
    client = get_ollama_client()

    # Call Ollama
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

    content = clean_json_response(content)

    try:
        data = json.loads(content)

    except json.JSONDecodeError as error:

        print("\n========== INVALID SCORING RESPONSE ==========\n")
        print(content)
        print("\n==============================================\n")

        raise ValueError(
            "Ollama returned invalid JSON during recommendation scoring."
        ) from error

    scored_data = data.get(
        "scored_recommendations",
        []
    )

    scored_recommendations = []

    for item in scored_data:

        scored_recommendations.append(
            ScoredRecommendation(**item)
        )

    return scored_recommendations