import json

from config.settings import OLLAMA_MODEL
from llm.client import get_ollama_client

from llm.prompts import (
    build_challenge_detection_prompt
)

from models.challenges import BusinessChallenge


def detect_challenges(
    company_name,
    research,
    analysis
):
    """
    Detect business challenges using AI.
    """

    prompt = build_challenge_detection_prompt(
        company_name=company_name,
        research=research,
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

    try:
        data = json.loads(content)

    except json.JSONDecodeError as error:

        print("\nINVALID CHALLENGE JSON:\n")
        print(content)

        raise ValueError(
            "Ollama returned invalid JSON for challenge detection."
        ) from error

    challenges_data = data.get(
        "challenges",
        []
    )

    challenges = []

    for item in challenges_data:

        challenges.append(
            BusinessChallenge(**item)
        )

    return challenges