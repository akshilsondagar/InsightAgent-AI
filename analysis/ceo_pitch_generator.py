import json

from config.settings import OLLAMA_MODEL
from llm.client import get_ollama_client
from llm.prompts import build_ceo_pitch_prompt

from models.ceo_pitch import CEOPitch


def convert_to_dict(data):
    """
    Convert Pydantic models into dictionaries.
    """

    if data is None:
        return None

    if hasattr(data, "model_dump"):
        return data.model_dump()

    if isinstance(data, list):
        return [
            convert_to_dict(item)
            for item in data
        ]

    if isinstance(data, dict):
        return {
            key: convert_to_dict(value)
            for key, value in data.items()
        }

    return data


def clean_json_response(content):
    """
    Clean JSON returned by Ollama.
    """

    content = content.strip()

    if content.startswith("```json"):
        content = content[7:].strip()

    elif content.startswith("```"):
        content = content[3:].strip()

    if content.endswith("```"):
        content = content[:-3].strip()

    return content


def generate_ceo_pitch(
    company_name,
    analysis,
    challenges,
    scored_recommendations
):
    """
    Generate CEO-level strategic pitch.
    """

    # --------------------------------------------------------
    # Validate company name
    # --------------------------------------------------------

    if not company_name:
        raise ValueError(
            "Company name cannot be empty."
        )

    # --------------------------------------------------------
    # Validate Ollama model
    # --------------------------------------------------------

    if not OLLAMA_MODEL:
        raise ValueError(
            "OLLAMA_MODEL is empty. "
            "Check config/settings.py and .env."
        )

    # --------------------------------------------------------
    # Convert data
    # --------------------------------------------------------

    analysis_data = convert_to_dict(
        analysis
    )

    challenges_data = convert_to_dict(
        challenges
    )

    recommendations_data = convert_to_dict(
        scored_recommendations
    )

    # --------------------------------------------------------
    # Build prompt
    # --------------------------------------------------------

    prompt = build_ceo_pitch_prompt(
        company_name=company_name,
        analysis=analysis_data,
        challenges=challenges_data,
        scored_recommendations=recommendations_data
    )

    if not prompt.strip():
        raise ValueError(
            "CEO pitch prompt is empty."
        )

    # --------------------------------------------------------
    # Ollama client
    # --------------------------------------------------------

    client = get_ollama_client()

    # --------------------------------------------------------
    # Ollama request
    # --------------------------------------------------------

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

    # --------------------------------------------------------
    # Get response
    # --------------------------------------------------------

    content = response["message"]["content"]

    if not content or not content.strip():
        raise ValueError(
            "Ollama returned an empty CEO pitch."
        )

    content = clean_json_response(
        content
    )

    # --------------------------------------------------------
    # Parse JSON
    # --------------------------------------------------------

    try:

        pitch_data = json.loads(
            content
        )

    except json.JSONDecodeError as error:

        print(
            "\n========== INVALID CEO JSON =========="
        )

        print(content)

        print(
            "\n======================================"
        )

        raise ValueError(
            "Ollama returned invalid JSON for CEO pitch."
        ) from error

    # --------------------------------------------------------
    # Ensure required string fields
    # --------------------------------------------------------

    string_fields = [
        "executive_summary",
        "key_business_problem",
        "strategic_recommendation",
        "expected_business_value"
    ]

    for field in string_fields:

        value = pitch_data.get(
            field,
            ""
        )

        if isinstance(value, dict):

            pitch_data[field] = json.dumps(
                value,
                ensure_ascii=False
            )

        elif isinstance(value, list):

            pitch_data[field] = " ".join(
                str(item)
                for item in value
            )

        elif value is None:

            pitch_data[field] = ""

        else:

            pitch_data[field] = str(value)

    # --------------------------------------------------------
    # Ensure roadmap is a list
    # --------------------------------------------------------

    roadmap = pitch_data.get(
        "implementation_roadmap",
        []
    )

    if isinstance(roadmap, str):

        pitch_data[
            "implementation_roadmap"
        ] = [roadmap]

    elif not isinstance(roadmap, list):

        pitch_data[
            "implementation_roadmap"
        ] = []

    # --------------------------------------------------------
    # Ensure immediate steps are a list
    # --------------------------------------------------------

    next_steps = pitch_data.get(
        "immediate_next_steps",
        []
    )

    if isinstance(next_steps, str):

        pitch_data[
            "immediate_next_steps"
        ] = [next_steps]

    elif not isinstance(next_steps, list):

        pitch_data[
            "immediate_next_steps"
        ] = []

    # --------------------------------------------------------
    # Validate with Pydantic
    # --------------------------------------------------------

    return CEOPitch(
        **pitch_data
    )