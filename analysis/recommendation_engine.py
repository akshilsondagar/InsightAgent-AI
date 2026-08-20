from llm.client import get_ollama_client
from llm.prompts import build_recommendation_prompt
from llm.structured_output import extract_json

from models.analysis import CompanyAnalysis
from models.challenge import BusinessChallenge
from models.recommendation import AIRecommendation


def generate_recommendations(
    company_name: str,
    analysis: CompanyAnalysis,
    challenges: list[BusinessChallenge]
) -> list[AIRecommendation]:
    """
    Generate AI/ML recommendations for detected
    business challenges using Ollama.
    """

    if not challenges:
        return []

    client = get_ollama_client()

    analysis_summary = format_analysis(
        analysis
    )

    challenges_text = format_challenges(
        challenges
    )

    prompt = build_recommendation_prompt(
        company_name=company_name,
        challenges_text=challenges_text,
        analysis_summary=analysis_summary
    )

    response = client.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    response_text = response["message"]["content"]

    recommendation_data = extract_json(
        response_text
    )

    recommendations = recommendation_data.get(
        "recommendations",
        []
    )

    return [
        AIRecommendation(**recommendation)
        for recommendation in recommendations
    ]


def format_analysis(
    analysis: CompanyAnalysis
) -> str:
    """
    Convert CompanyAnalysis into readable text.
    """

    return f"""
Company Overview:
{analysis.company_overview}

Business Model Insights:
{format_list(analysis.business_model_insights)}

Market Trends:
{format_list(analysis.market_trends)}

Technology Insights:
{format_list(analysis.technology_insights)}

Key Observations:
{format_list(analysis.key_observations)}
"""


def format_challenges(
    challenges: list[BusinessChallenge]
) -> str:
    """
    Convert business challenges into readable text
    for the recommendation prompt.
    """

    if not challenges:
        return "No challenges detected."

    formatted = []

    for index, challenge in enumerate(
        challenges,
        start=1
    ):
        evidence_text = format_list(
            challenge.evidence
        )

        formatted.append(
            f"""
CHALLENGE {index}

Title:
{challenge.title}

Description:
{challenge.description}

Evidence:
{evidence_text}

Business Impact:
{challenge.impact}

Priority:
{challenge.priority}
"""
        )

    return "\n".join(formatted)


def format_list(items: list[str]) -> str:
    """
    Convert a list into readable bullet points.
    """

    if not items:
        return "- No information available"

    return "\n".join(
        f"- {item}"
        for item in items
    )